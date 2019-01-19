// 引用模板
import index from '../src/page/index.vue'
import content from '../src/page/content.vue'
import user from '../src/page/user.vue'
// 配置路由
export default [
  {
    path: '/',
    component: index
  },
  {
    path: '/content',
    component: content
  },{
    path: '/user',
    component: user
  }
]
