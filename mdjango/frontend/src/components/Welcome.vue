<template>
  <div id="welcome-interface">
    <el-container>
      <el-header style="align-self: center">
        <img src="../assets/logo.png"/>
      </el-header>

      <el-main>
        <h3 align="center">Welcome to </h3>
        <h1 align="center">M  O. V. A.</h1>
        <h3 align="center">your MOvie Visualization Analyse system</h3>
      </el-main>

      <el-footer>
        <el-row type="flex" justify="space-around">
          <el-col :span="6" :offset="2">
            <div class="sign-up">
              <el-button class="sign-btn" @click="toNewAccount" round>账号注册</el-button>
            </div>
          </el-col>
          <el-col :span="6" :offset="2">
            <div class="log-in">
              <el-button class="log-btn" @click="toSignIn" round>账号登录</el-button>
            </div>
          </el-col>
          <el-col :span="6" :offset="2">
            <div class="visitor">
              <el-button class="visit-btn" @click="visible = true" round>游客登录</el-button>
              <el-dialog class="visit-dlg" :visible.sync="visible" width="55%">
                <span>您将以游客身份登录，是否继续？</span>
                <span slot="footer" class="dialog-footer">
                  <el-button @click="visible = false" round>取 消</el-button>
                  <el-button type="primary" @click="toMainPage" round>确 定</el-button>
                </span>
              </el-dialog>
            </div>
          </el-col>
        </el-row>
      </el-footer>
    </el-container>
    <h6 align="center">Copyright © Software Engineering Group X</h6>
  </div>
</template>

<script>
export default {
  data () {
    return {
      visible: false
    }
  },
  methods: {
    toNewAccount: function () {
      this.$router.push({path: '/new'})
    },
    toSignIn: function () {
      localStorage.setItem('VisitorMode', '0')
      this.$router.push({path: '/login'})
    },
    toMainPage: function () {
      this.visible = false
      localStorage.setItem('VisitorMode', '1')
      this.$router.push({path: '/main'})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#welcome-interface{
  background: #2d3436;
  max-width: 800px;
  margin: 0 auto;
}
.el-header {
  margin-top: 20px;
}
.el-footer {
  background-color: #20bf6b;
  color: #333;
  line-height: 60px;
  margin-bottom: 20px;
}
p {
  font-family: "Hiragino Sans GB",monospace;
}
h1 {
  color: white;
  font-family: Futura,sans-serif;
}
h3 {
  color: white;
  font-family: Futura,sans-serif;
}
h6 {
  color: white;
  font-family: Arial,sans-serif;
}
.sign-btn {
  color: #dfe6e9;
  background: #20bf6b;
}
.log-btn {
  color: #dfe6e9;
  background: #20bf6b;
}
.visit-btn {
  color: #dfe6e9;
  background: #20bf6b;
}
</style>
