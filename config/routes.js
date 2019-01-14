// 引用模板
import index from '../src/page/index.vue'
import content from '../src/page/content.vue'
// 配置路由
export default [
  {
    path: '/',
    component: index
  },
  {
    path: '/content',
    component: content
  },
]
