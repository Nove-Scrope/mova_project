<!--suppress ALL -->
<template>
  <div id="net-crawler">
    <main-header></main-header>
    <el-container>
      <el-header></el-header>

      <el-main>
        <h1>Ready to get the movie data?</h1>
        <h4>启动网络爬虫将会占用您较长的时间...</h4>
        <h5>（若点击返回则可使用现有数据进行分析）</h5>
      </el-main>

      <el-footer>
        <el-row :type="'flex'">
          <el-col :span="12" align="center">
            <div class="start">
              <el-button class="start-btn" @click="startCrawler" round>开始</el-button>
            </div>
          </el-col>
          <el-col :span="12" align="center">
            <div class="cancel">
              <el-button class="cancel-btn" @click="toMainPage" round>返回</el-button>
            </div>
          </el-col>
        </el-row>
        <h6 align="center" style="color: #ffffff">Copyright © Software Engineering Group X</h6>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import MainHeader from './MainHeader'

export default {
  components: {
    'main-header': MainHeader
  },
  data () {
    return {
      visible: true
    }
  },
  methods: {
    startCrawler: function () {
      console.log('Crawler is running...')
      if (localStorage.getItem('VisitorMode') === '1') {
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
      } else {
        var msg
        var crawlRequest = {
          a: 4,
          start: '1'
        }
        var postData = this.$qs.stringify(crawlRequest)
        this.axios.post('movie/', postData).then(function (response) {
          console.log(response.data)
          msg = response.data.toString()
        }).catch(function (error) {
          console.log(error)
        })
        alert(msg)
      }
    },
    toMainPage: function () {
      this.$router.push({path: '/main'})
    }
  }
}
</script>

<style scoped>
#net-crawler {
  background: #2d3436;
  max-width: 800px;
  margin: 0 auto;
}

.el-main {
  margin-top: 20px;
}
.el-footer {
  background-color: #747d8c;
  color: #333;
  line-height: 60px;
  margin-top: 50px;
  margin-bottom: 20px;
}
h1 {
  color: white;
  font-family: Monaco,monospace;
  margin-top: 1px;
}
h4, h5 {
  color: white;
  font-family: "Hiragino Sans GB",monospace;
}
.start-btn {
  color: #dfe6e9;
  border-color: #20bf6b;
  border-width: 3px;
  background: #747d8c;
}
.cancel-btn {
  color: #dfe6e9;
  border-color: #20bf6b;
  border-width: 3px;
  background: #747d8c;
}
</style>
