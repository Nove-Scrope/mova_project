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
        <div id="wordChart" style="width: 600px;height: 400px;margin-top: 20px;"></div>
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
  name: 'performanceRankWordCloud',
  components: {
    'main-header': MainHeader
  },
  data () {
    return {
      checked: 0,
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
      drawRequest.func_selected = '7'
      drawRequest.year = this.rankYearSelected
      drawRequest.top_x = this.rankSelected
      var postData = this.$qs.stringify(drawRequest)
      var wordChart = this.$echarts.init(document.getElementById('wordChart'))
      wordChart.setOption({
        title: {
          text: 'XXXX年演员出演TOP',
          textStyle: {
            color: '#ffffff'
          }
        },
        tooltip: {
          show: true
        },
        toolbox: {
          feature: {
            saveAsImage: {
              iconStyle: {
                normal: {
                  color: '#333'
                }
              }
            }
          }
        },
        series: [{
          name: '演员出演排名TOP',
          type: 'wordCloud',
          gridSize: 20,
          sizeRange: [12, 50],
          rotationRange: [0, 0],
          shape: 'circle',
          data: [],
          textStyle: {
            normal: {
              color: function (v) {
                let color = ['#27D38A', '#FFCA1C', '#5DD1FA', '#F88E25', '#47A0FF', '#FD6565']
                let num = Math.floor(Math.random() * (5 + 1))
                return color[num]
              }
            },
            emphasis: {
              shadowBlur: 5,
              shadowColor: '#bdc3c7'
            }
          }
        }]
      })
      wordChart.showLoading({
        text: '加载中',
        color: '#20bf6b',
        textColor: '#ffffff',
        maskColor: '#2d3436'
      })
      this.axios.post('movie/', postData).then(function (response) {
        console.log(response.data)
        var index
        var tmpList = []
        var length = response.data['y_axis'].length
        for (index = 0; index < length; index++) {
          var tmpObject = {
            value: 0,
            name: ''
          }
          tmpObject.value = response.data['y_axis'][index]
          tmpObject.name = response.data['x_axis'][index]
          tmpList.push(tmpObject)
        }
        console.log(tmpList)
        wordChart.hideLoading()
        wordChart.setOption({
          title: {
            text: response.data['chart_title']
          },
          series: {
            data: tmpList
          }
        })
      }).catch(function (error) {
        console.log(error)
      })
    },
    drawWord: function () {
      var wordChart = this.$echarts.init(document.getElementById('wordChart'))
      var option = {
        title: {
          text: 'XXXX年演员出演TOP',
          textStyle: {
            color: '#ffffff'
          }
        },
        tooltip: {
          show: true
        },
        toolbox: {
          feature: {
            saveAsImage: {
              iconStyle: {
                normal: {
                  color: '#333'
                }
              }
            }
          }
        },
        series: [{
          name: '演员出演排名TOP',
          type: 'wordCloud',
          gridSize: 20,
          sizeRange: [12, 50],
          rotationRange: [0, 0],
          shape: 'circle',
          data: [],
          textStyle: {
            normal: {
              color: function (v) {
                let color = ['#27D38A', '#FFCA1C', '#5DD1FA', '#F88E25', '#47A0FF', '#FD6565']
                let num = Math.floor(Math.random() * (5 + 1))
                return color[num]
              }
            },
            emphasis: {
              shadowBlur: 5,
              shadowColor: '#bdc3c7'
            }
          }
        }]
      }
      wordChart.setOption(option)
    }
  },
  mounted () {
    this.drawWord()
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
  margin-top: 30px;
  background: white;
}
</style>
