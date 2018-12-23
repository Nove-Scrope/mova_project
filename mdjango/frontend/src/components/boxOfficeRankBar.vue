<template>
  <div id="box-office-rank">
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
        <div id="barChart" style="width: 500px;height: 300px;margin-top: 20px;margin-left: 80px;"></div>
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
  name: 'boxOfficeRankBar',
  components: {
    'main-header': MainHeader
  },
  data () {
    return {
      rankYearSelected: '',
      rankSelected: 0,
      years: [
        {label: '2015', value: '2015'},
        {label: '2016', value: '2016'},
        {label: '2017', value: '2017'},
        {label: '2018', value: '2018'}
      ],
      rank: [
        {label: '前3名', value: 3},
        {label: '前5名', value: 5},
        {label: '前10名', value: 10}
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
      drawRequest.func_selected = '2'
      drawRequest.year = this.rankYearSelected
      drawRequest.top_x = this.rankSelected
      var postData = this.$qs.stringify(drawRequest)
      var barChart = this.$echarts.init(document.getElementById('barChart'), 'light')
      barChart.setOption({
        title: {
          text: '',
          textStyle: {
            color: '#ffffff'
          }
        },
        tooltip: {},
        legend: {
          data: ['题材'],
          textStyle: {
            color: '#ffffff'
          }
        },
        xAxis: {
          data: []
        },
        yAxis: {},
        series: [{
          name: '票房',
          type: 'bar',
          data: []
        }],
        textStyle: {
          color: '#ffffff'
        },
        itemStyle: {
          shadowBlur: 100,
          shadowColor: '#000000'
        }
      })
      barChart.showLoading({
        text: '加载中',
        color: '#20bf6b',
        textColor: '#ffffff',
        maskColor: '#2d3436'
      })
      this.axios.post('movie/', postData).then(function (response) {
        console.log(response.data)
        barChart.hideLoading()
        barChart.setOption({
          title: {
            text: response.data['chart_title']
          },
          xAxis: {
            data: response.data['x_axis']
          },
          series: [{
            name: '票房',
            data: response.data['y_axis']
          }]
        })
      }).catch(function (error) {
        console.log(error)
      })
    },
    drawBar: function () {
      var barChart = this.$echarts.init(document.getElementById('barChart'), 'light')
      var option = {
        title: {
          text: 'XXXX年X月/季度题材票房比例',
          textStyle: {
            color: '#ffffff'
          }
        },
        tooltip: {},
        legend: {
          data: ['题材'],
          textStyle: {
            color: '#ffffff'
          }
        },
        xAxis: {
          data: [],
          axisLabel: {
            rotate: 30,
            fontSize: 10
          }
        },
        yAxis: {},
        series: [{
          name: '票房',
          type: 'bar',
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
      barChart.setOption(option)
    }
  },
  mounted () {
    this.drawBar()
  }
}
</script>

<style scoped>
#box-office-rank{
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
</style>
