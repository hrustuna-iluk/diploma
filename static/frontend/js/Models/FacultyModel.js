var FacultyModel = Backbone.Model.extend ({

    urlRoot: '/api/faculty/',

    defaults: function() {
        return {
            title: "",
            amountOfWeekInSecondSemester: 0,
            amountOfWeekInFirstSemester: 0,
            endSecondSemester: null,
            endFirstSemester: null,
            startSecondSemester: null,
            startFirstSemester: null,
            dean: TeacherModel
        }
    },

    initialize: function () {
        /*this.on('change:startFirstSemester', function () {
          this.set('startFirstSemester', new Date(this.get('startFirstSemester')));
        });
        this.on('change:startSecondSemester', function () {
          this.set('startSecondSemester', new Date(this.get('startSecondSemester')));
        });
        this.on('change:endFirstSemester', function () {
            this.set('endFirstSemester', new Date(this.get('endFirstSemester')));
        });
        this.on('change:endSecondSemester', function () {
            this.set('endSecondSemester', new Date(this.get('endSecondSemester')));
        });*/
    },

    parse: function(resp) {
        if (_.isArray(resp)) {
            resp = resp[0];
        }
        /*resp.startFirstSemester = new Date(resp.startFirstSemester);
        resp.startSecondSemester = new Date(resp.startSecondSemester);
        resp.endFirstSemester = new Date(resp.endFirstSemester);
        resp.endSecondSemester = new Date(resp.endSecondSemester);*/
        return resp;
    }

});