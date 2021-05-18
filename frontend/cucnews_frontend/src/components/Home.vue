<template>
    <el-container class="home-container">
        <el-header class="is-always-shadow">
            <div>
                <img src="@/assets/logo1.png" class="logoImg" alt="">
                <h4 style="margin:0">阿巴阿巴舆情分析</h4>
            </div>
        </el-header>
        <el-container style="padding-top:60px">
            <el-aside :width="isCollapse ? '70px' : '200px'">
               <el-menu
                active-text-color="%409eff"
                unique-opened
                router
                :collapse="isCollapse"
                :collapse-transition="false"
                :default-active="$route.path">
                    <el-menu-item
                    v-for="menu in menuList"
                    :index="menu.index + ''"
                    :key="menu.id"
                    >
					<b><i class="el-icon-star-off" /></b>
                        <span>{{menu.name}}</span>
                    </el-menu-item>
                </el-menu>
            </el-aside>
            <el-main>
                <router-view></router-view>
            </el-main>
        </el-container>
		<el-footer>
			<div style="text-align:center">
				<p style="margin:0">Copyright (c) 2021 来自 吴雨晨 刘听宇</p>
			</div>
		</el-footer>
    </el-container>
</template>

<script>
export default {
  data () {
    return {
      menuList: [
		 {id: 0, name: '中传要闻', index: '/cucnews'},
		 {id: 1, name: '知乎热榜', index: '/zhihu'},
		 {id: 2, name: '微博详情', index: '/weibo'},
		 {id: 3, name: '微博用户', index: '/weibouser'},
		 {id: 4, name: '微博专题', index: '/weibotopic'},
		 {id: 5, name: 'JOJO人物关系图谱', index: '/jojo'}
      ],
      isCollapse: false
    }
  }
}
</script>
<style lang='less' scoped>
.el-header {
    position: fixed;
    background-color: #fff;
    z-index: 999;
    width: 100%;
    display: flex;
    justify-content: space-between;
    padding-left: 0;
    align-items: center;
    //color: #fff;
    font-size: 20px;
    > div {
        display: flex;
        // 垂直居中
        align-items: center;
    }
    > span {
        margin-left: 20px;
    }
    box-shadow: 10px 5px 5px lightgray;
}
.el-aside {
    // background-color: #333744;
    border-right: 1px solid #6a6a6a;
    .el-menu {
        border-right: none;
    }
}
.el-menu-item:hover span {
  opacity: 1;
  text-indent: 0px;
  -webkit-transition: all 300ms ease-in-out;
  -moz-transition: all 300ms ease-in-out;
  -ms-transition: all 300ms ease-in-out;
  -o-transition: all 300ms ease-in-out;
  transition: all 300ms ease-in-out;
}
.home-container {
    height: 100%;
}
.logoImg {
    width: auto;
    height: 60px;
    display:inline-block;
    margin:0px 20px
}
.el-footer {
  height: 20px;
}
</style>
