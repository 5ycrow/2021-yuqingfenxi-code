<template>
  <div class="heHelloWorld">
    {{msg}}
  </div>
</template>

<script>
import api from '@/axios/api'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: ''
    }
  },
  mounted () {
    this.getMessage()
  },
  methods:{
	getMessage(){
		api.getMessage().then(res => {
		  console.log(res)
		  if (res.status !== 1) {
		    this.loading = false
		    this.$message.error('信息获取失败')
		  }
		  this.msg = res.info
		})
	}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>