import Vue from 'vue'
import Router from 'vue-router'
import Welcome from '../components/Welcome'
import SignUp from '../components/SignUp'
import LogIn from '../components/LogIn'
import MainPage from '../components/MainPage'
import ChangePassword from '../components/ChangePassword'
import ForgetPassword from '../components/ForgetPassword'
import GetData from '../components/GetData'
import BoxOfficeRateBar from '../components/boxOfficeRateBar'
import BoxOfficeRatePie from '../components/boxOfficeRatePie'
import BoxOfficeTendencyLine from '../components/boxOfficeTendencyLine'
import BoxOfficeRankBar from '../components/boxOfficeRankBar'
import BoxOfficeRankWordCloud from '../components/boxOfficeRankWordCloud'
import PerformanceRankBar from '../components/performanceRankBar'
import PerformanceRankWordCloud from '../components/performanceRankWordCloud'
import DiagramSelect from '../components/DiagramSelect'
import MovieSearch from '../components/MovieSearch'

Vue.use(Router)

export default new Router({
  routes: [
    {path: '/', component: Welcome},
    {path: '/new', component: SignUp},
    {path: '/login', component: LogIn},
    {path: '/main', component: MainPage},
    {path: '/change', component: ChangePassword},
    {path: '/reset', component: ForgetPassword},
    {path: '/crawler', component: GetData},
    {path: '/bar-box-office-rate', component: BoxOfficeRateBar},
    {path: '/pie-box-office-rate', component: BoxOfficeRatePie},
    {path: '/line-box-office-tend', component: BoxOfficeTendencyLine},
    {path: '/bar-box-office-rank', component: BoxOfficeRankBar},
    {path: '/word-cloud-box-office-rank', component: BoxOfficeRankWordCloud},
    {path: '/bar-performance-rank', component: PerformanceRankBar},
    {path: '/word-cloud-performance-rank', component: PerformanceRankWordCloud},
    {path: '/select', component: DiagramSelect},
    {path: '/search', component: MovieSearch}
  ],
  mode: 'history'
})
