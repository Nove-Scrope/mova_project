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
              <el-button class="draw-btn" @click="postData" round>画图</el-button>
            </div>
          </el-col>
        </el-row>
        <div class="graph">
          <el-tabs  tab-position="left">
            <el-tab-pane label="pic">
              <img src="../diagrams/pie.svg"/>
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
  name: 'boxOfficeBar',
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
    postData: function () {
      console.log('Hello!')
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
  margin-top: 30px;
  background: white;
}
</style>
