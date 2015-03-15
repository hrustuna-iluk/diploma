var MotherModel = Backbone.Model.extend ({

    urlRoot: '/api/parents/',

    defaults: function() {
       return{
           fullName: "",
           phone: "",
           position: ""
       }


    }
});