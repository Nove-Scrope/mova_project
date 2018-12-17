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
              <el-button class="draw-btn" @click="postData" round>画图</el-button>
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
    postData: function () {
      console.log('Hello!')
    }
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
