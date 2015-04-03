var AddPublicOrdersOfGroupFormView = BaseView.extend({

    template: _.template($("#addPublicOrdersFormTemplate").html()),

    optionTemplate: _.template($("#optionPublicOrdersStudentTemplate").html()),

    initialize: function(options) {
        this.group = options.group;
        this.collection = options.collection;
        this.collection.reset().fetch({
            data: {
               group: this.group.get('id')
            },
            success: $.proxy(function () {
                    this._fillLeaderList();
                    this._fillDeputyHeadmanList();
                    this._fillOrganizerList();
                    this._fillCulturalWorkList();
                    this._fillHealthWorkList();
                    this._fillEditorialBoardList();
                    this._fillOtherTasksWorkList();
         }, this)
        });
    },

    _attachEvents: function() {
        this.$('#addPublicOrders').on('click', $.proxy(this._changeGroupData, this));
    },

    _changeGroupData: function() {
        this.group.set({
            leader: this.$('#groupLeaderSelect').val(),
            deputyHeadman: this.$('#groupDeputyHeadmanSelect').val(),
            organizer: this.$('#groupOrganizerSelect').val(),
            culturalWork: this.$('#groupCulturalWorkSelect').val(),
            healthWork: this.$('#groupHealthWorkSelect').val(),
            editorialBoard: this.$('#groupEditorialBoardSelect').val(),
            otherTasks: this.$('#groupOtherTasksSelect').val()
        });
        this.group.save();
    },

    _fillLeaderList: function() {
        this.collection.each(function(model) {
            this.$('#groupLeaderSelect').append(this.optionTemplate(model.toJSON()));
        }, this);
    },

     _fillDeputyHeadmanList: function() {
        this.collection.each(function(model) {
            this.$('#groupDeputyHeadmanSelect').append(this.optionTemplate(model.toJSON()));
        }, this);
    },

     _fillOrganizerList: function() {
        this.collection.each(function(model) {
            this.$('#groupOrganizerSelect').append(this.optionTemplate(model.toJSON()));
        }, this);
    },

     _fillCulturalWorkList: function() {
        this.collection.each(function(model) {
            this.$('#groupCulturalWorkSelect').append(this.optionTemplate(model.toJSON()));
        }, this);
    },

     _fillHealthWorkList: function() {
        this.collection.each(function(model) {
            this.$('#groupHealthWorkSelect').append(this.optionTemplate(model.toJSON()));
        }, this);
    },

    _fillEditorialBoardList: function() {
        this.collection.each(function(model) {
            this.$('#groupEditorialBoardSelect').append(this.optionTemplate(model.toJSON()));
        }, this);
    },

    _fillOtherTasksWorkList: function() {
        this.collection.each(function(model) {
            this.$('#groupOtherTasksSelect').append(this.optionTemplate(model.toJSON()));
        }, this);
    },


    render: function() {
        this.$el.html(this.template);
        this._attachEvents();
        return this;
    }

});