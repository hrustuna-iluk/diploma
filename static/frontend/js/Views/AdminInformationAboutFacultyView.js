var AdminInformationAboutFacultyView = BaseView.extend({

    template: _.template($("#adminAllFacultyInfoTemplate").html()),

    initialize: function(options) {
        this.model = options.faculty;
    },

    _attachEvents: function() {
        this.$('#saveFacultyInformation').on('click', $.proxy(this._addInformation, this))
    },

    _formatDate: function (date) {
        if (!date) return;

        var year = date.getFullYear();
        var month = date.getMonth();
        var day = date.getDate();
        return [
            year,
            month < 10 ? '0' + month : month,
            day < 10 ? '0' + day : day
        ].join('-')
    },

    _facultyData: function() {
        this.$("#facultyTitle").val(this.model.get('title'));
        this.$("#firstSemesterStart").val(this.model.get('startFirstSemester'));
        this.$("#firstSemesterEnd").val(this.model.get('endFirstSemester'));
        this.$("#secondSemesterStart").val(this.model.get('startSecondSemester'));
        this.$("#secondSemesterEnd").val(this.model.get('endSecondSemester'));
    },

    _addInformation: function() {
        this.model.set({
            title: this.$("#facultyTitle").val(),
            startFirstSemester: this.$("#firstSemesterStart").val(),
            endFirstSemester: this.$("#firstSemesterEnd").val(),
            startSecondSemester: this.$("#secondSemesterStart").val(),
            endSecondSemester: this.$("#secondSemesterEnd").val()
        });

        this.model.save();
    },

    render: function() {
        this.$el.html(this.template);
        this._attachEvents();
        this._facultyData();
        return this;
    }

});