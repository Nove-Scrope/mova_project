<template>
    <div id="box-office-rate">
      <el-container>
        <el-header>
          <main-header></main-header>
        </el-header>
        <el-main>
          <el-row type="flex" justify="space-around">
            <el-col :span="6">
              <div class="year-select">
                <el-select v-model="yearSelected" placeholder="请选择年份">
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
              <div class="quarter-select">
                <el-select v-model="quarterSelected" placeholder="请选择季度">
                  <el-option
                    v-for="item in quarters"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="month-select">
                <el-select v-model="monthSelected" placeholder="请选择月份">
                  <el-option
                    v-for="item in months"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
              </div>
            </el-col>
            <el-col :span="4">
              <div class="draw">
                <el-button class="draw-btn" @click="drawPic" round>画图</el-button>
              </div>
            </el-col>
          </el-row>
        <div id="pieChart" style="width: 600px;height: 400px;margin-top: 20px;"></div>
        <!-- <div class="graph">
          <el-tabs  tab-position="left">
            <el-tab-pane label="pic">
            </el-tab-pane>
          </el-tabs>
        </div> -->
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
  name: 'boxOfficeRatePie',
  components: {
    'main-header': MainHeader
  },
  data () {
    return {
      yearSelected: '',
      quarterSelected: '',
      monthSelected: '',
      years: [
        {label: '2015', value: '2015'},
        {label: '2016', value: '2016'},
        {label: '2017', value: '2017'},
        {label: '2018', value: '2018'}
      ],
      quarters: [
        {value: 0, label: '无'},
        {value: '1', label: '第1季度'},
        {value: '2', label: '第2季度'},
        {value: '3', label: '第3季度'},
        {value: '4', label: '第4季度'}
      ],
      months: [
        {label: '无', value: '0'},
        {label: '1', value: '1'},
        {label: '2', value: '2'},
        {label: '3', value: '3'},
        {label: '4', value: '4'},
        {label: '5', value: '5'},
        {label: '6', value: '6'},
        {label: '7', value: '7'},
        {label: '8', value: '8'},
        {label: '9', value: '9'},
        {label: '10', value: '10'},
        {label: '11', value: '11'},
        {label: '12', value: '12'}
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
      drawRequest.func_selected = '5'
      drawRequest.year = this.firstYearSelected
      drawRequest.quarter = this.secondYearSelected
      drawRequest.month = this.thirdYearSelected
      var postData = this.$qs.stringify(drawRequest)
      this.axios.post('movie/', postData).then(function (response) {
        console.log(response)
      }).catch(function (error) {
        console.log(error)
      })
    },
    drawPie: function () {
      var pieChart = this.$echarts.init(document.getElementById('pieChart'))
      var option = {
        title: {
          text: 'ECharts 入门示例',
          textStyle: {
            color: '#ffffff'
          }
        },
        series: [{
          name: '访问来源',
          type: 'pie',
          roseType: 'angle',
          radius: '65%',
          data: [
            {value: 235, name: '视频广告'},
            {value: 254, name: '联盟广告'},
            {value: 310, name: '邮件营销'},
            {value: 335, name: '直接访问'},
            {value: 400, name: '搜索引擎'}
          ]
        }],
        textStyle: {
          color: '#ffffff'
        },
        itemStyle: {
          color: '#e74c3c',
          shadowBlur: 100,
          shadowColor: '#000000'
        },
        visualMap: {
          show: false,
          min: 80,
          max: 600,
          inRange: {
            colorLightness: [0, 1]
          }
        }
      }
      pieChart.setOption(option)
    }
  },
  mounted () {
    this.drawPie()
  }
}
</script>

<style scoped>
#box-office-rate{
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
