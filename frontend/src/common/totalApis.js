export default class totalApis {
  static apis() {
    return Object.freeze({
      // ユーザー情報API
      userCreate: "/api/user/create/",
      userList: "/api/user/list/",
      userDelete: "/api/user/",
      userMyself: "/api/user/myself/",
      // タスク情報API
      taskCreate: "/api/task/create/",
      taskList: "/api/task/list/",
      taskDelete: "/api/task/",
      taskUpdate: "/api/task/",
      // トークン
      token: "/token/",
      tokenVerify: "/token/verify/",
      tokenRefresh: "/token/refresh/",
    })
  }
}