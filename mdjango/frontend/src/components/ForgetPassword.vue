<!--suppress ALL -->
<template>
  <div id="forget-pwd">
    <el-container>
      <el-header align="center">
        <h1>Reset your password!</h1>
      </el-header>

      <el-main>
        <el-row :gutter="10">
          <el-col :span="4" :push="3">
            <div class="usrName-lbl" align="center">
              <h4>用户名:</h4>
            </div>
          </el-col>
          <el-col :span="12" :push="3">
            <div class="usrName-ipt">
              <el-input class="usrName" placeholder="请输入用户名" v-model="usrNameInput"
                        size="medium" clearable required />
            </div>
          </el-col>
        </el-row>

        <el-row :gutter="10">
          <el-col :span="4" :push="3">
            <div class="pwdchg-lbl" align="center">
              <h4>新密码:</h4>
            </div>
          </el-col>
          <el-col :span="12" :push="3">
            <div class="pwdchg-ipt">
              <el-input class="pwdnew" placeholder="请输入新密码" v-model="pwdNew" type="text"
                        size="medium" minlength="4" clearable required />
            </div>
          </el-col>
        </el-row>

        <el-row :gutter="10">
          <el-col :span="4" :push="3">
            <div class="pwdcheck-lbl" align="center">
              <h4>验证码:</h4>
            </div>
          </el-col>
          <el-col :span="6" :push="3">
            <div class="pwdcheck-ipt">
              <el-input class="pwdcheck" placeholder="请输入4位验证码" type="text" v-model="verifyInput"
                        size="medium" minlength="4" clearable required />
            </div>
          </el-col>
          <el-col :span="4" :push="3">
            <div class="identifybox" @click="refreshCode">
              <s-identify :identifyCode="identifyCode"></s-identify>
            </div>
          </el-col>
        </el-row>
      </el-main>

      <el-footer>
        <el-row :type="'flex'" :justify="'space-around'">
          <el-col :span="12" align="center">
            <div class="confirm-info">
              <el-button class="confirm-btn" v-on:click="resetPwdCheckin" round>重置</el-button>
            </div>
          </el-col>
          <el-col :span="12" align="center">
            <div class="cancel">
              <el-button class="cancel-btn" @click="toHomePage" round>取消</el-button>
            </div>
          </el-col>
        </el-row>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import SIdentify from './verifyCode'

export default {
  components: {
    's-identify': SIdentify
  },
  data () {
    return {
      usrName: localStorage.getItem('name'),
      passwd: localStorage.getItem('password'),
      usrNameInput: '',
      pwdNew: '',
      verifyInput: '',
      identifyCode: '',
      identifyCodes: '1234567890'
    }
  },
  methods: {
    resetPwdCheckin: function () {
      if (this.usrNameInput !== this.usrName) {
        this.$alert('用户名错误！', '修改失败', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'error',
              message: '请重新输入用户名'
            })
          },
          showClose: false
        })
      } else if (this.verifyInput !== this.identifyCode) {
        this.$alert('您输入的验证码有误！', '修改失败', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'error',
              message: '请重新输入验证码'
            })
          },
          showClose: false
        })
      } else {
        localStorage.setItem('password', this.pwdNew)
        this.$router.push({path: '/login'})
      }
    },
    pwdState: function (data) {
      this.visible = !(data === 'show')
    },
    toHomePage: function () {
      this.$router.push({path: '/login'})
    },
    randomNum: function (min, max) {
      return Math.floor(Math.random() * (max - min) + min)
    },
    refreshCode: function () {
      this.identifyCode = ''
      this.makeCode(4)
    },
    makeCode: function (l) {
      for (let i = 0; i < l; i++) {
        this.identifyCode += this.identifyCodes[this.randomNum(0, this.identifyCodes.length)]
      }
      console.log(this.identifyCode)
    }
  },
  created () {

  },
  mounted () {
    // 验证码初始化
    this.identifyCode = ''
    this.makeCode(4)
  }
}
</script>

<style scoped>
#forget-pwd{
  background: #2d3436;
  max-width: 800px;
  margin: 0 auto;
}
.el-header {
  background-color: #20bf6b;
  color: #333;
  line-height: 60px;
  margin-top: 20px;
}
.el-footer {
  background-color: #747d8c;
  color: #333;
  line-height: 60px;
  margin-top: 5px;
  margin-bottom: 20px;
}
h1 {
  color: white;
  font-family: Monaco,monospace;
  margin-top: 1px;
}
h4 {
  color: white;
  font-family: "Hiragino Sans GB",monospace;
}
.usrName, .pwdnew, .pwdcheck {
  margin-top: 15px;
}
.confirm-btn {
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
i {
  width: 10px;
}
.identifybox{
  display: flex;
  justify-content: space-between;
  margin-top:13px;
  cursor: pointer;
}
.iconstyle{
  color: #0984e3;
}
</style>
