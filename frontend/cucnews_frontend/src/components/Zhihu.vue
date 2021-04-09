<template>
<div>
	<div style="width: 300px;display: flex;float: right;">
		<el-input v-model="wanted" placeholder="关键字"></el-input>
		<el-button type="primary" @click="onSubmit">查询</el-button>
	</div>
	
	<img src="../../static/news.jpg" v-show="picshow"></img>
  <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column type="expand">
      <template slot-scope="props">
		  <el-form label-position="left" inline class="demo-table-expand">
		  			<el-form-item label="图片" style="width: 200px;">
		  			  <el-image
		  			  style="width: 200px;height: 200px;"
		  			  :src="props.row.imgUrl"
		  			  :preview-src-list="[props.row.imgUrl]"></el-image>
		  			</el-form-item>
		  </el-form>
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="内容" style="width: 1200px;">
            <span>{{ props.row.content }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      label="ID"
      prop="id" width="150">
    </el-table-column>
    <el-table-column
      label="topic"
      prop="topic">
    </el-table-column>

	<el-table-column
	  label="hotValue"
	  prop="hotValue" width="150">
	</el-table-column>
	<el-table-column
	  label="contentUrl"
	  prop="contentUrl" width="150">
	  <template slot-scope="{row}">
	      <el-link :href="row.contentUrl" target="_blank" class="buttonText"  type="primary" :underline="false">详情</el-link>
	  </template>
	</el-table-column>
  </el-table>
  <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-sizes="[10, 20, 30, 50, 100]"
      :page-size="pageSize"
      layout="total, sizes, prev, pager, next, jumper"
      :total="tableTotal">
  </el-pagination>
</div>
</template>

<style>
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>

<script>
	import api from '@/axios/api'
  export default {
    data() {
      return {
        tableData: [],
		wanted:'',
		picshow:false,
		handleList: [],
		// 当前页
		currentPage: 1,
		// 每页多少条
		pageSize: 10,
		tableTotal:0
      }
    },
	mounted () {
	  this.getZhihu()
	},
	methods:{
		getZhihu(){
			api.getZhihu({offset:(this.currentPage-1)*this.pageSize,limit:this.pageSize}).then(res => {
			  console.log(res)
			  if (res.status !== 1) {
			    this.loading = false
			    this.$message.error('获取失败')
			  }
			  this.tableData = res.zhihu_list
			  this.tableTotal=res.total
			})
		},
		onSubmit() {
				api.searchZhihu(JSON.stringify({wanted: this.wanted,offset:(this.currentPage-1)*this.pageSize,limit:this.pageSize})).then(res => {
				// console.log(res)
				  if (res.status !== 1) {
				    this.loading = false
				    this.$message.error('查询失败')
				  }
				  this.picshow=true
				  this.tableData = res.zhihu_list
				  this.tableTotal=res.total
				})
		      },
			   handleSizeChange(val) {
				  this.pageSize = val;
				  this.getZhihu()
			  },
			  // 当前页
			  handleCurrentChange(val) {
				  this.currentPage = val;
				  this.getZhihu()
			  }
	}
  }
</script>