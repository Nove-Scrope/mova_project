<template>
  <div id="main-page">
    <main-header></main-header>
    <el-container>
      <el-header></el-header>
      <el-main>
        <div class="pic" align="center">
          <img src="../assets/logo.png"/>
          <h3>向Vue.js致谢</h3>
        </div>
      </el-main>
      <el-footer>
        <h6 align="center" style="color: #ffffff">Copyright © Software Engineering Group X</h6>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import MainHeader from './MainHeader'

export default {
  name: 'MainPage',
  components: {
    'main-header': MainHeader
  },
  data () {
    return {

    }
  }
}
</script>

<style scoped>
#main-page{
  background: #2d3436;
  max-width: 800px;
  margin: 0 auto;
}
.el-footer {
  margin: 0 auto;
}
h3 {
  color: #ffffff;
  margin-top: 1px;
  margin-bottom: 1px;
}
</style>
