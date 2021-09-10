const app = Vue.createApp({
    data() {
      return {
        show_modal_forgot:false,
        value_username: '',
        value_email :''
      }
    },
    methods: {
        send_mail() {
            fetch("http://127.0.0.1:8000/home/forgot_pass/", {
                method: "POST",
                headers : new Headers({"Content-Type" : "application/x-www-form-urlencoded"}),
                body: `email=${this.value_email}&username=${this.value_username}`
            }).then(response => response.json())
            .then(response => alert(JSON.stringify(response)))
            .catch(error => alert("Erreur : " + error));
            
            //application/x-www-form-urlencoded
        }
    },
    compilerOptions: {
        delimiters: ["[[", "]]"]
      }
  })
app.mount("#app")