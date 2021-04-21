<template>
<div>
  <el-table
    :data="tableData"
    style="width: 100%">
   <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="个人简介" style="width: 1200px;">
            <span>{{ props.row.description }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      label="ID"
      prop="id" width="150">
    </el-table-column>
    <el-table-column
      label="用户ID"
      prop="nickname">
    </el-table-column>
	<el-table-column
	  label="性别"
	  prop="gender" width="150">
	</el-table-column>
	<el-table-column
	  label="地点"
	  prop="location" width="150">
	</el-table-column>
	<el-table-column
	  label="生日"
	  prop="birthday" width="150">
	</el-table-column>
	<el-table-column
	  label="认证"
	  prop="verified_reason" width="150">
	</el-table-column>
	<el-table-column
	  label="教育经历"
	  prop="education" width="150">
	</el-table-column>
	<el-table-column
	  label="工作"
	  prop="work" width="150">
	</el-table-column>
	<el-table-column
	  label="微博数量"
	  prop="weibo_num" width="150">
	</el-table-column>
	<el-table-column
	  label="关注数量"
	  prop="following" width="150">
	</el-table-column>
	<el-table-column
	  label="粉丝"
	  prop="followers" width="150">
	</el-table-column>
<!-- 	<el-table-column
	  label="contentUrl"
	  prop="contentUrl" width="150">
	  <template slot-scope="{row}">
	      <el-link :href="row.contentUrl" target="_blank" class="buttonText"  type="primary" :underline="false">详情</el-link>
	  </template>
	</el-table-column> -->
<!-- 	<el-table-column
	  label="NLP"
	  prop="nlp" width="150">
	     <template slot-scope="snownlp">
	         <el-button type="primary" size="mini" round @click="onNlp(snownlp.row)">NLP一键分析</el-button>
	     </template>
	</el-table-column> -->
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
		tableTotal:0,
		sentiments: 0,
		keywords: '123',
		summary:'123'
      }
    },
	mounted () {
	  this.getWeiboUser()
	},
	methods:{
		getWeiboUser(){
			api.getWeiboUser({offset:(this.currentPage-1)*this.pageSize,limit:this.pageSize}).then(res => {
			  console.log(res)
			  if (res.status !== 1) {
			    this.loading = false
			    this.$message.error('获取失败')
			  }
			  this.tableData = res.weibouser_list
			  this.tableTotal=res.total
			})
		},
			  // onNlp(row) {
			  //   api.nlpApi(JSON.stringify({text: row.content})).then(res => {
			  // 	if (res.status !== 1) {
			  // 	  this.loading = false
			  // 	  this.$message.error('text获取失败')
			  // 	}
			  // 	this.sentiments=res.sentiments
			  // 	this.keywords = res.keywords
			  // 	this.summary=res.summary
			  	
			  // 	this.$alert("情感分析指数："+this.sentiments+"</br>"+"关键词："+this.keywords+"</br>"+"摘要："+this.summary, '分析结果', {
			  // 			dangerouslyUseHTMLString: true,
			  // 	          confirmButtonText: '确定',
			  // 	          callback: action => {
			  // 	            this.$message({
			  // 	              type: 'info',
			  // 	              message: `分析完成`
			  // 	            });
			  // 	          }
			  // 	        });
			  	
			  //   })
			  // },
			   handleSizeChange(val) {
				  this.pageSize = val;
				  this.getWeiboUser()
			  },
			  // 当前页
			  handleCurrentChange(val) {
				  this.currentPage = val;
				  this.getWeiboUser()
			  }
	}
  }
</script>