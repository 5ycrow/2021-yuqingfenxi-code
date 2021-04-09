import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Cucnews from '@/components/Cucnews'
import Zhihu from '@/components/Zhihu'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
	mode:'history',
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
		{ path: '/zhihu', component: Zhihu }
	  ]
	}
  ]
})