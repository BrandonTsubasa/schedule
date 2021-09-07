import Vue from "vue";
import Router from "vue-router";
import VueRouter from "vue-router";
import totalPages from "@/common/totalPages.js";
import Task from "@/views/Task.vue";
import TaskCalendar from "@/views/TaskCalendar.vue";
import SignUp from "@/views/auth/SignUp.vue";
import SignIn from "@/views/auth/SignIn.vue";
import BootstrapVue from "bootstrap-vue";
import User from "@/views/user/User.vue";
import UserNameEdit from "@/views/user/UserNameEdit.vue";
import UserEmailEdit from "@/views/user/UserEmailEdit.vue";
import UserPasswordEdit from "@/views/user/UserPasswordEdit.vue";


Vue.use(Router);
Vue.use(BootstrapVue);

export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      component: totalPages.pages().top,
    },
    {
      path: "/Task",
      component: Task,
    },
    {
      path: "/TaskCalendar",
      component: TaskCalendar
    },
    {
      path: "/SignUp",
      component: SignUp
    },
    {
      path: "/SignIn",
      component: SignIn
    },
    {
      path: "/User",
      component: User
    },
    {
      path: "/UserNameEdit",
      component: UserNameEdit
    },
    {
      path: "/UserEmailEdit",
      component: UserEmailEdit
    },
    {
      path: "/UserPasswordEdit",
      component: UserPasswordEdit
    },
  ],
});
