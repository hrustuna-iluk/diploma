var ClassModel = Backbone.Model.extend ({

    urlRoot: '/api/class',

    defaults: function() {
        return {
            subject: "",
            type: "",
            teacher: TeacherModel,
            classroom: '',
            day: "",
            numberOfWeek: 0,
            number: 0,
            group: GroupModel
        }
    },

    setSubject: function(value) {
        this.set('subject', value);
    },

    setType: function(value) {
        this.set('type', value);
    },

    setTeacher: function(value) {
        this.set('teacher', value);
    },

    setClassroom: function(value) {
        this.set('classroom', value);
    },

    setDay: function(value) {
        this.set('day', value);
    },

    setNumberOfWeek: function(value) {
        this.set('numberOfWeek', value);
    },

    setNumber: function(value) {
        this.set('number', value);
    },

    getSubject: function() {
        return this.get('subject');
    },

    getType: function() {
        return this.get('type');
    },

    getTeacher: function() {
        return this.get('teacher');
    },

    getClassroom: function() {
        return this.get('classroom');
    },

    getDay: function() {
        return this.get('day');
    },

    getNumberOfWeek: function() {
        return this.get('numberOfWeek');
    },

    getNumber: function() {
        return this.get('number');
    }

});