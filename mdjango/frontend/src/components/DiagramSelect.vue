<!--suppress ALL -->
<template>
  <div id="diagram-select">
    <main-header></main-header>
    <el-container>
      <el-header></el-header>

      <el-main>
        <el-alert class="alert-msg"
          title="此功能将保存最近一次生成的选定图表"
          type="warning" show-icon
          close-text="知道了">
        </el-alert>
        <el-form class="select-form" label-width="80px">
          <el-form-item class="checkbox-group" label="柱状图">
            <el-checkbox-group v-model="diagramChecked" fill="#20bf6b">
              <el-checkbox-button label="1">题材票房比例</el-checkbox-button>
              <el-checkbox-button label="2">电影票房top排名</el-checkbox-button>
              <el-checkbox-button label="3">演员出演top排名</el-checkbox-button>
            </el-checkbox-group>
          </el-form-item>
          <el-form-item class="checkbox-group" label="折线图">
            <el-checkbox-group v-model="diagramChecked" fill="#20bf6b">
              <el-checkbox-button label="4">电影票房变化趋势</el-checkbox-button>
            </el-checkbox-group>
          </el-form-item>
          <el-form-item class="checkbox-group" label="饼图">
            <el-checkbox-group v-model="diagramChecked" fill="#20bf6b">
              <el-checkbox-button label="5">题材票房比例</el-checkbox-button>
            </el-checkbox-group>
          </el-form-item>
          <el-form-item class="checkbox-group" label="词云">
            <el-checkbox-group v-model="diagramChecked" fill="#20bf6b">
              <el-checkbox-button label="6">电影票房top排名</el-checkbox-button>
              <el-checkbox-button label="7">演员出演top排名</el-checkbox-button>
            </el-checkbox-group>
          </el-form-item>
        </el-form>
      </el-main>

      <el-footer>
        <el-row :type="'flex'">
          <el-col :span="12" align="center">
            <div class="download">
              <el-button class="download-btn" @click="startDownload" round>下载</el-button>
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
      // barChecked: [],
      // lineChecked: [],
      // pieChecked: [],
      // wordCloudChecked: [],
      diagramChecked: []
    }
  },
  methods: {
    startDownload: function () {
      console.log('Diagrams are downloading...')
      if (localStorage.getItem('VisitorMode') === '1') {
        this.$alert('您当前为游客，无法使用！', '下载失败', {
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
        // this.diagramChecked.push.apply(this.diagramChecked, this.barChecked)
        // this.diagramChecked.push.apply(this.diagramChecked, this.barChecked)
        // this.diagramChecked.push.apply(this.diagramChecked, this.barChecked)
        // this.diagramChecked.push.apply(this.diagramChecked, this.barChecked)
        this.diagramChecked.sort()
        var selected = ''
        selected = this.diagramChecked.join('')
        // alert(selected)
        var downloadRequest = {
          a: 3,
          chart_download: '0'
        }
        downloadRequest.chart_download = selected
        var postData = this.$qs.stringify(downloadRequest)
        this.axios.post('movie/', postData).then(function (response) {
          console.log(response)
        }).catch(function (error) {
          console.log(error)
        })
      }
    },
    toMainPage: function () {
      this.$router.push({path: '/main'})
    }
  }
}
</script>

<style scoped>
#diagram-select {
  background: #2d3436;
  max-width: 800px;
  margin: 0 auto;
}
.select-form {
  background: white;
  border: solid 5px #20bf6b;
  border-radius: 10px;
}
.el-main {
  margin-top: 10px;
}
.el-footer {
  background-color: #747d8c;
  color: #333;
  line-height: 60px;
  margin-top: 0px;
  margin-bottom: 20px;
}
h1 {
  color: white;
  font-family: Monaco,monospace;
  margin-top: 1px;
}
h4, h5{
  color: white;
  font-family: "Hiragino Sans GB",monospace;
}
.download-btn {
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
.checkbox-group {
  margin-top: 10px;
}
  .alert-msg {
    margin-bottom: 10px;
  }
</style>
