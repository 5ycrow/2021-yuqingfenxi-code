import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Cucnews from '@/components/Cucnews'
import Zhihu from '@/components/Zhihu'
import Home from '@/components/Home'
import WeiBo from '@/components/WeiBo'
import WeiBoUser from '@/components/WeiBoUser'
import WeiBoTopic from '@/components/WeiBoTopic'
import JoJo from '@/components/JoJo'
import JoJo2 from '@/components/JoJo2'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/index',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/',
      name: 'Home',
      redirect: '/cucnews',
      component: Home,
      children: [
        { path: '/cucnews', component: Cucnews },
        { path: '/zhihu', component: Zhihu },
        { path: '/weibo', component: WeiBo },
        { path: '/weibouser', component: WeiBoUser },
        { path: '/weibotopic', component: WeiBoTopic },
        { path: '/jojo', component: JoJo },
        { path: '/jojo2', component: JoJo2 }
      ]
    }
  ]
})
