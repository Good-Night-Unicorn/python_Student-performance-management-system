const base = {
    get() {
        return {
            url : "http://localhost:8080/djangogpkm2/",
            name: "djangogpkm2",
            // 退出到首页链接
            indexUrl: ''
        };
    },
    getProjectName(){
        return {
            projectName: "用Python设计学生成绩管理系统"
        } 
    }
}
export default base
