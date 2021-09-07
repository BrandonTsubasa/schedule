export default class totalPages{
    // TOP画面のページを列挙
    static pages() {
        return Object.freeze({
            Top: "/",
            Task: "Task",
            TaskCalendar: "TaskCalendar",
        })
    }
    // ハンバーガーメニューに表示するページを列挙
    static menuPages() {
        return Object.freeze({
            SignUp: "SignUp",
            SignIn: "SignIn",
            User: "User",
        })
    }
    // ユーザー編集画面のページを列挙
    static userSettings() {
        return Object.freeze({
            UserNameEdit: "UserNameEdit",
            UserEmailEdit: "UserEmailEdit",
            UserPasswordEdit: "UserPasswordEdit",
        })
    }
    // バリデーションのルールを列挙
    static validateNames() {
        return Object.freeze({
            required: "required",
            requiredEmail: "required|email",
            requiredPassword: "required|min:6|max:20",
            requiredConfirm: "required|confirmed:",
            
        });
    }
}