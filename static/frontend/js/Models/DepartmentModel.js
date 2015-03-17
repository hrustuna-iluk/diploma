var DepartmentModel = Backbone.Model.extend ({

    urlRoot: '/api/department/',

    defaults: function() {
        return {
            title: "",
            headOfDepartment: null

        }
    },


    setTitle: function(value) {
        this.set('title', value);
    },

    getTitle: function() {
        return this.get('title');
    },

    setHeadOfDepartment: function(value) {
        this.set('headOfDepartment', value);
    },

    getHeadOfDepartment: function() {
        return this.get('headOfDepartment');
    }
});