<!--suppress ALL -->
<template>
  <div id="chg-passwd">
    <el-container>
      <el-header align="center">
        <h1>Reset your password!</h1>
      </el-header>

      <el-main>
        <el-row :gutter="10">
          <el-col :span="4" :push="3">
            <div class="passwd-lbl" align="center">
              <h4>旧密码:</h4>
            </div>
          </el-col>
          <el-col :span="12" :push="3">
            <div class="passwd-ipt">
              <el-input class="passwd" placeholder="请输入旧密码" v-model="pwdInput" type="text"
                        size="medium" minlength="4" clearable required>
              </el-input>
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
              <h4>确认密码:</h4>
            </div>
          </el-col>
          <el-col :span="12" :push="3">
            <div class="pwdcheck-ipt">
              <el-input class="pwdcheck" placeholder="再次输入密码" v-model="pwdCheck" type="password"
                        size="medium" minlength="4" clearable required />
            </div>
          </el-col>
        </el-row>
      </el-main>

      <el-footer>
        <el-row :type="'flex'" :justify="'space-around'">
          <el-col :span="12" align="center">
            <div class="confirm-info">
              <el-button class="confirm-btn" v-on:click="newPwdCheckin" round>修改</el-button>
            </div>
          </el-col>
          <el-col :span="12" align="center">
            <div class="cancel">
              <el-button class="cancel-btn" @click="toMainPage" round>取消</el-button>
            </div>
          </el-col>
        </el-row>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  data () {
    return {
      usrName: localStorage.getItem('name'),
      passwd: localStorage.getItem('password'),
      pwdInput: '',
      pwdNew: '',
      visible: true
    }
  },
  methods: {
    newPwdCheckin: function () {
      if (this.pwdInput !== this.passwd) {
        this.$alert('您输入的旧密码有误！', '修改失败', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'error',
              message: '请重新输入旧密码'
            })
          },
          showClose: false
        })
      } else if (this.pwdCheck !== this.pwdInput) {
        this.$alert('您输入的确认密码有误！', '修改失败', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'error',
              message: '请重新输入确认密码'
            })
          },
          showClose: false
        })
      } else {
        localStorage.setItem('password', this.pwdNew)
        this.$router.push({path: '/main'})
      }
    },
    toMainPage: function () {
      this.$router.push({path: '/main'})
    }
  }
}
</script>

<style scoped>
#sign-up{
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
.el-main{
  margin-top: 20px;
}
.el-footer {
  background-color: #747d8c;
  color: #333;
  line-height: 60px;
  margin-top: 50px;
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
.passwd, .pwdnew, .pwdcheck {
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
</style>
