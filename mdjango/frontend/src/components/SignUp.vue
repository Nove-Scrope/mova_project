<!--suppress ALL -->
<template>
  <div id="sign-up">
    <el-container>
      <el-header align="center">
        <h1>Sign up for your account!</h1>
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
              <el-input class="usrName" placeholder="请输入用户名" v-model="usrName"
                        size="medium" clearable required />
            </div>
          </el-col>
        </el-row>

        <el-row :gutter="10">
          <el-col :span="4" :push="3">
            <div class="passwd-lbl" align="center">
              <h4>密码:</h4>
            </div>
          </el-col>
          <el-col :span="12" :push="3">
            <div class="passwd-ipt-hide" v-if="visible">
              <el-input class="passwd" placeholder="请输入密码" v-model="passwd" type="password"
                        size="medium" minlength="4" clearable required>
                <i class="el-icon-view" title="显示密码" @click="pwdState('show')" slot="append"/>
              </el-input>
            </div>
            <div class="passwd-ipt-show" v-else>
              <el-input class="passwd" placeholder="请输入密码" v-model="passwd" type="text"
                        size="medium" minlength="4" clearable required>
                <i class="el-icon-view" title="隐藏密码" @click="pwdState('hide')" slot="append"/>
              </el-input>
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
        <el-row type="flex" justify="space-around">
          <el-col :span="12" align="center">
            <div class="confirm-info">
              <el-button class="confirm-btn" v-on:click="pwdCheckin" round>确认</el-button>
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
export default {
  data () {
    return {
      usrName: '',
      passwd: '',
      pwdCheck: '',
      visible: true
    }
  },
  methods: {
    pwdCheckin: function () {
      if (this.pwdCheck !== this.passwd) {
        this.$alert('您输入的密码不一致！', '注册失败', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'error',
              message: '请重新输入密码'
            })
          },
          showClose: false
        })
      } else {
        localStorage.setItem('name', this.usrName)
        localStorage.setItem('password', this.passwd)
        this.$router.push({path: '/'})
      }
    },
    pwdState: function (data) {
      this.visible = !(data === 'show')
    },
    toHomePage: function () {
      this.$router.push({path: '/'})
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
.usrName, .passwd, .pwdcheck {
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
</style>
