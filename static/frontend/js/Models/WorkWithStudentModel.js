var WorkWithStudentModel = Backbone.Model.extend ({

    urlRoot: '/api/studentwork/',

    defaults: function() {
        return {
            text: "",
            year: "",
            group: GroupModel
        }
    },

    setTitle: function(value) {
        this.set('text', value);
    },

    getTitle: function() {
        return this.get('text');
    },

    setYear: function(value) {
        this.set('year', value);
    },

    getYear: function() {
        return this.get('year');
    }

});