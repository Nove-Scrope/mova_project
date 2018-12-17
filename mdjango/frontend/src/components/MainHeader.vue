<template>
  <div id="main-header">
    <el-container>
      <el-header>
        <h1 class="title-head" align="center">M  O. V. A.</h1>
        <el-menu
          default-active="$route.path" class="el-menu-demo" mode="horizontal"
          background-color="#2d3436" text-color="#ffffff" active-text-color="#2ed573" router>
          <el-menu-item index="/crawler">
            <span>数据获取</span>
            <i class="el-icon-document" slot=""></i>
          </el-menu-item>
          <el-menu-item index="/search">
            <span>搜索电影</span>
            <i class="el-icon-search" slot=""></i>
          </el-menu-item>
          <el-submenu index="diagram">
            <template slot="title">
              <span>图表工作台</span>
            </template>
            <el-submenu index="/bar">
              <template slot="title">柱状图</template>
              <el-menu-item index="/bar/box-office-rate">题材票房比例</el-menu-item>
              <el-menu-item index="/bar/box-office-rank">电影票房top排名</el-menu-item>
              <el-menu-item index="/bar/performance-rank">演员出演top排名</el-menu-item>
            </el-submenu>
            <el-submenu index="/line">
              <template slot="title">折线图</template>
              <el-menu-item index="/line/box-office-tend">电影票房变化趋势</el-menu-item>
            </el-submenu>
            <el-submenu index="/pie">
              <template slot="title">饼图</template>
              <el-menu-item index="/pie/box-office-rate">题材票房比例</el-menu-item>
            </el-submenu>
            <el-submenu index="/word-cloud">
              <template slot="title">词云</template>
              <el-menu-item index="/word-cloud/box-office-rank">电影票房top排名</el-menu-item>
              <el-menu-item index="/word-cloud/performance-rank">演员出演top排名</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-menu-item index="/select">
            <template slot="title">
              <span>图表下载坞</span>
            </template>
          </el-menu-item>
          <el-submenu index="options">
            <template slot="title">
              <span>个人中心</span>
              <i class="el-icon-setting" slot=""></i>
            </template>
            <el-menu-item index="/change" @click="checkVisitor">修改密码</el-menu-item>
            <el-menu-item index="/">退出登录</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-header>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'MainHeader',
  data () {
    return {

    }
  },
  methods: {
    checkVisitor: function () {
      if (localStorage.getItem('VisitorMode') === '1') {
        this.$router.push({path: '/main'})
        this.$alert('您当前为游客，无法使用！', '启动失败', {
          cancelButtonText: '返回',
          callback: action => {
            this.$message({
              type: 'warning',
              message: '请注册账号！'
            })
          },
          showClose: false
        })
      }
    }
  }
}
</script>

<style scoped>
#main-header{
  background: #2d3436;
  max-width: 800px;
  margin: 0 auto;
}
.title-head {
  background-color: #20bf6b;
  color: #ffffff;
  font-family: Futura, sans-serif;
  line-height: 30px;
  margin-top: 20px;
}
</style>
