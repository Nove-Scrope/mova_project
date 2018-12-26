<template>
  <div id="box-office-tend">
    <el-container>
      <el-header>
        <main-header></main-header>
      </el-header>
      <el-main>
        <el-row type="flex" justify="space-around">
          <el-col :span="6">
            <div class="year-select-1">
              <el-select v-model="firstYearSelected" placeholder="请选择年份">
                <el-option
                  v-for="item in yearsNeeded"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </div>
          </el-col>
          <el-col :span="6">
            <div class="year-select-2">
              <el-select v-model="secondYearSelected" placeholder="请选择年份">
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
            <div class="year-select-3">
              <el-select v-model="thirdYearSelected" placeholder="请选择年份">
                <el-option
                  v-for="item in years"
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
        <div id="lineChart" style="width: 700px;height: 400px;margin-top: 50px;"></div>
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
  name: 'boxOfficeTendencyLine',
  components: {
    'main-header': MainHeader
  },
  data () {
    return {
      firstYearSelected: '',
      secondYearSelected: '',
      thirdYearSelected: '',
      yearsNeeded: [
        {label: '2015', value: '2015'},
        {label: '2016', value: '2016'},
        {label: '2017', value: '2017'},
        {label: '2018', value: '2018'}
      ],
      years: [
        {label: '无', value: '0'},
        {label: '2015', value: '2015'},
        {label: '2016', value: '2016'},
        {label: '2017', value: '2017'},
        {label: '2018', value: '2018'}
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
      drawRequest.func_selected = '4'
      drawRequest.year = this.firstYearSelected
      drawRequest.quarter = this.secondYearSelected
      drawRequest.month = this.thirdYearSelected
      var postData = this.$qs.stringify(drawRequest)
      var lineChart = this.$echarts.init(document.getElementById('lineChart'), 'light')
      lineChart.setOption({
        title: {
          text: '',
          textStyle: {
            color: '#ffffff'
          }
        },
        legend: {
          orient: 'horizontal',
          x: 'top',
          top: '5%',
          left: '50%',
          padding: [10, 5],
          textStyle: {
            color: '#ffffff'
          },
          data: []
        },
        tooltip: {
          trigger: 'axis'
        },
        toolbox: {
          show: true,
          feature: {
            mark: {
              show: true
            },
            dataView: {
              show: true,
              readOnly: false
            },
            restore: {
              show: true
            },
            saveAsImage: {
              show: true
            }
          }
        },
        calculable: true,
        xAxis: {
          data: [],
          axisLabel: {
            rotate: 30,
            fontSize: 10
          }
        },
        yAxis: {},
        textStyle: {
          color: '#ffffff'
        },
        itemStyle: {
          shadowBlur: 100,
          shadowColor: '#000000'
        }
      })
      lineChart.showLoading({
        text: '加载中',
        color: '#20bf6b',
        textColor: '#ffffff',
        maskColor: '#2d3436'
      })
      var legends = []
      legends.push(this.firstYearSelected)
      legends.push(this.secondYearSelected)
      legends.push(this.thirdYearSelected)
      legends.sort()
      this.axios.post('movie/', postData).then(function (response) {
        console.log(response.data)
        lineChart.hideLoading()
        lineChart.setOption({
          title: {
            text: response.data['chart_title']
          },
          legend: {
            data: legends
          },
          xAxis: {
            data: response.data['x_axis']
          },
          series: [{
            name: legends[0],
            type: 'line',
            data: response.data['y_axis'][0]
          },
          {
            name: legends[1],
            type: 'line',
            data: response.data['y_axis'][1]
          },
          {
            name: legends[2],
            type: 'line',
            data: response.data['y_axis'][2]
          }]
        })
      }).catch(function (error) {
        console.log(error)
      })
    },
    drawLine: function () {
      var lineChart = this.$echarts.init(document.getElementById('lineChart'), 'light')
      var option = {
        title: {
          text: 'XXXX至XXXX每月电影票房变化趋势（单位： 万元）'
        },
        tooltip: {
          trigger: 'axis'
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: []
        },
        yAxis: {
          type: 'value',
          axisTick: {
            alignWithLabel: true,
            lineStyle: {
              color: '#ffffff',
              type: 'dotted'
            }
          }
        },
        series: [{
          name: '',
          type: 'line',
          data: []
        }],
        textStyle: {
          color: '#ffffff'
        },
        itemStyle: {
          shadowBlur: 100,
          shadowColor: '#000000'
        }
      }
      lineChart.setOption(option)
    }
  },
  mounted () {
    this.drawLine()
  }
}
</script>

<style scoped>
#box-office-tend{
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
