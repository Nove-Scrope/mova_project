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
                <el-button class="draw-btn" v-on:click="drawPic" round>画图</el-button>
              </div>
            </el-col>
          </el-row>
          <!-- <div class="graph"> -->
          <!-- <img src="../diagrams/boxoffice_ratio_bar.png" /> -->
          <!-- <el-tabs  tab-position="left">
            <el-tab-pane label="pic"> -->
          <div id="barChart" style="width: 500px;height: 300px;margin-top: 20px;"></div>
            <!-- </el-tab-pane>
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
  name: 'boxOfficeBar',
  components: {
    'main-header': MainHeader
  },
  data () {
    return {
      yearSelected: '',
      quarterSelected: '',
      monthSelected: '',
      imgShow: 0,
      years: [
        {label: '2015', value: '2015'},
        {label: '2016', value: '2016'},
        {label: '2017', value: '2017'},
        {label: '2018', value: '2018'}
      ],
      quarters: [
        {value: '0', label: '无'},
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
      var flag = 0
      var drawRequest = {
        a: 2,
        func_selected: '0',
        year: '0',
        quarter: '0',
        month: '0',
        top_x: 0
      }
      drawRequest.func_selected = '1'
      drawRequest.year = this.yearSelected
      drawRequest.quarter = this.quarterSelected
      drawRequest.month = this.monthSelected
      var postData = this.$qs.stringify(drawRequest)
      this.axios.post('movie/', postData).then(function (response) {
        console.log(response)
        flag = 1
      }).catch(function (error) {
        console.log(error)
      })
      this.imgShow = flag
    },
    drawBar: function () {
      var barChart = this.$echarts.init(document.getElementById('barChart'), 'light')
      var option = {
        title: {
          text: 'ECharts 入门示例',
          textStyle: {
            color: '#ffffff'
          }
        },
        tooltip: {},
        legend: {
          data: ['销量'],
          textStyle: {
            color: '#ffffff'
          }
        },
        xAxis: {
          data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
        },
        yAxis: {},
        series: [{
          name: '销量',
          type: 'bar',
          data: [5, 20, 36, 10, 10, 20]
        }],
        textStyle: {
          color: '#ffffff'
        },
        itemStyle: {
          shadowBlur: 100,
          shadowColor: '#000000'
        }
      }
      barChart.setOption(option)
    }
  },
  mounted () {
    this.drawBar()
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
/* .graph {
  margin-top: 20px;
  background: white;
} */
</style>
