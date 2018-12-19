<template>
  <div id="performance-rank">
    <el-container>
      <el-header>
        <main-header></main-header>
      </el-header>
      <el-main>
        <el-row type="flex" justify="space-around">
          <el-col :span="6">
            <div class="year-select">
              <el-select v-model="rankYearSelected" placeholder="请选择年份">
                <el-option
                  v-for="item in years"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </div>
          </el-col>
          <el-col :span="6">
            <div class="rank-select">
              <el-select v-model="rankSelected" placeholder="请选择排名">
                <el-option
                  v-for="item in rank"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </div>
          </el-col>
          <el-col :span="6">
            <div class="draw">
              <el-button class="draw-btn" @click="drawPic" round>画图</el-button>
            </div>
          </el-col>
        </el-row>
        <div class="graph">
          <el-tabs  tab-position="left">
            <el-tab-pane label="pic">
            </el-tab-pane>
          </el-tabs>
        </div>
      </el-main>
      <el-footer>
        <h6 align="center">Copyright © Software Engineering Group X</h6>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import MainHeader from './MainHeader'

export default {
  name: 'performanceRankBar',
  components: {
    'main-header': MainHeader
  },
  data () {
    return {
      rankYearSelected: '',
      rankSelected: '',
      years: [
        {label: '2015', value: '2015'},
        {label: '2016', value: '2016'},
        {label: '2017', value: '2017'},
        {label: '2018', value: '2018'}
      ],
      rank: [
        {label: '前3名', value: '3'},
        {label: '前5名', value: '5'},
        {label: '前10名', value: '10'}
      ]
    }
  },
  methods: {
    drawPic: function () {
      var drawRequest = {
        a: 2,
        func_selected: '0',
        year: '0',
        quarter: '0',
        month: '0',
        top_x: 0
      }
      drawRequest.func_selected = '3'
      drawRequest.year = this.rankYearSelected
      drawRequest.top_x = this.rankSelected
      var postData = this.$qs.stringify(drawRequest)
      this.axios.post('movie/', postData).then(function (response) {
        console.log(response)
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
#performance-rank{
  background: #2d3436;
  max-width: 800px;
  margin: 0 auto;
}
.el-header {
  margin-bottom: auto;
}
.el-main{
  margin-top: 100px;
}
.el-footer {
  margin-top: 30px;
  margin-bottom: 5px;
}
h1 {
  color: white;
  font-family: Monaco,monospace;
  margin-top: 1px;
}
h6 {
  color: #ffffff;
}
.graph {
  margin-top: 20px;
  background: white;
}
</style>
