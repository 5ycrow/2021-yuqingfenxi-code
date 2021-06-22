<template>
<div>
	<h3>微博热门话题：JOJO</h3>
  <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="内容" style="width: 1200px;">
            <span>{{ props.row.微博正文 }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      label="微博ID"
      prop="user_id">
    </el-table-column>
    <el-table-column
      label="用户ID"
      prop="用户昵称">
    </el-table-column>
	<el-table-column
	  label="艾特用户"
	  prop="艾特用户" >
	</el-table-column>
	<el-table-column
	  label="位置"
	  prop="发布位置" >
	</el-table-column>
	<el-table-column
	  label="话题"
	  prop="话题" >
	</el-table-column>

	<el-table-column
	  label="发布时间"
	  prop="发布时间" >
	</el-table-column>
	<el-table-column
	  label="发布工具"
	  prop="发布工具">
	</el-table-column>
	<el-table-column
	  label="点赞数量"
	  prop="点赞数" >
	</el-table-column>
	<el-table-column
	  label="转发数量"
	  prop="转发数" >
	</el-table-column>
	<el-table-column
	  label="评论数量"
	  prop="评论数" >
	</el-table-column>

	<el-table-column
	  label="NLP"
	  prop="nlp" >
	     <template slot-scope="snownlp">
	         <el-button type="primary" size="mini" round @click="onNlp(snownlp.row)">NLP一键分析</el-button>
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
  data () {
    return {
      tableData: [],
      wanted: '',
      picshow: false,
      handleList: [],
      // 当前页
      currentPage: 1,
      // 每页多少条
      pageSize: 10,
      tableTotal: 0,
      sentiments: 0,
      keywords: '123',
      summary: '123'
    }
  },
  mounted () {
	  this.getWeiboTopic()
  },
  methods: {
    getWeiboTopic () {
      api.getJoJo3({offset: (this.currentPage - 1) * this.pageSize, limit: this.pageSize}).then(res => {
			  console.log(res)
			  if (res.status !== 1) {
			    this.loading = false
			    this.$message.error('获取失败')
			  }
			  this.tableData = res.jojo_list
			  this.tableTotal = res.total
      })
    },
			  onNlp (row) {
			    api.nlpApi(JSON.stringify({text: row.微博正文})).then(res => {
			  	if (res.status !== 1) {
			  	  this.loading = false
			  	  this.$message.error('text获取失败')
			  	}
			  	this.sentiments = res.sentiments
			  	this.keywords = res.keywords
			  	this.summary = res.summary

			  	this.$alert('情感分析指数：' + this.sentiments + '</br>' + '关键词：' + this.keywords + '</br>' + '摘要：' + this.summary, '分析结果', {
			  			dangerouslyUseHTMLString: true,
			  	          confirmButtonText: '确定',
			  	          callback: action => {
			  	            this.$message({
			  	              type: 'info',
			  	              message: `分析完成`
			  	            })
			  	          }
			  	        })
			    })
			  },
			   handleSizeChange (val) {
				  this.pageSize = val
				  this.getWeiboTopic()
			  },
			  // 当前页
			  handleCurrentChange (val) {
				  this.currentPage = val
				  this.getWeiboTopic()
			  }
  }
}
</script>
