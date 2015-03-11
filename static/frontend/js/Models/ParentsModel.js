var ParentsModel = Backbone.Model.extend ({

    urlRoot: '/api/parents',

    defaults: function() {
       return{
           fullName: "",
           phone: "",
           position: "",
           student: StudentModel
       }


    }
});