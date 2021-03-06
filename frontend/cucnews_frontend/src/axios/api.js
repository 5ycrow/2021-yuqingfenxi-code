/**
 * api接口统一管理
 */
import {get, post} from './axios'
/**
 * @param {string} params
 * 我们定义了一个topics方法
 * 这个方法有一个参数params
 * params是我们请求接口时携带的参数对象
 * 而后调用了我们封装的post方法
 * post方法的第一个参数是我们的接口地址
 * 第二个参数是topics的params参数
 * 即请求接口时携带的参数对象
 * 最后通过export导出topics。
 * 示例: export const login = params => post('/login', params)
 */
export default {
  getMessage () {
    return get('/cucnews/index')
  },
  getNews (params) {
    return get('/cucnews/getnews', params)
  },
  searchNews (data) {
    return post('/cucnews/getnews', data)
  },
  getZhihu (params) {
    return get('/zhihu/hotnews', params)
  },
  getWeibo (params) {
    return get('/weibo/info', params)
  },
  getWeiboUser (params) {
    return get('/weibouser/info', params)
  },
  getWeiboTopic (params) {
	  return get('/weibotopic/info', params)
  },
  searchZhihu (data) {
    return post('/zhihu/hotnews', data)
  },
  nlpApi (data) {
    return post('/nlp/snownlp', data)
  },
  getJoJo () {
    return get('/jojo/getjojo')
  },
  getJoJo2 () {
    return get('/jojo/getjojo2')
  },
  getJoJo3 (params) {
	  return get('/jojo/info', params)
  }
}
