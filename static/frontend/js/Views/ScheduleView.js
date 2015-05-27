var ScheduleView = BaseView.extend({

    template:  _.template($("#scheduleTemplate").html()),

    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],

    classes: [],

    initialize: function(options) {
        this.collection = options.collection;
        this.teachersCollection = options.teachersCollection;
        this.group = options.group;
        this.collection.reset().fetch({
            data: {group: this.group.get('id')},
            success: $.proxy(this._buildScheduler, this)
        });
    },

    _attachEvents: function() {
        this.$('.deleteSchedule').on('click', $.proxy(this._wantDeleteSchedule, this));
        this.$('select').on('change', $.proxy(this._buildScheduler, this));
    },

    _buildScheduler: function () {
        this.classes = [];
        var numberOfClass = 1;
        this.$('table tbody').empty();
        while (numberOfClass !== 7) {
            this.$('table tbody').append(
                new ClassesView({
                    parentView: this,
                    numberOfClass: numberOfClass,
                    numberOfWeek: this.$('select').val(),
                    group: this.group,
                    collection: this.collection,
                    teachersCollection: this.teachersCollection
                }).render().$el
            );
            numberOfClass++;
        }
        this._fillClassesCollection();
    },

    _fillClassesCollection: function() {
         this.collection.each($.proxy(function(model) {
             if(model.getNumberOfWeek() == this.$('select').val()){
                 this.classes[model.getNumber()-1][this.days.indexOf(model.getDay())].setModel(model);
             }
         }, this), this);
    },

    _wantDeleteSchedule: function() {
        if(!confirm("Ви дійсно хочете видалити розклад?")) {
            return;
        }
        this.collection.reset();
        this._deleteSchedule();
    },

    _deleteSchedule: function() {
        $.post('/app/deleteSchedule/', {group: this.group.get('id')}, $.proxy(function (resp) {
            alert(resp.message);
            this._buildScheduler();
        }, this));
    },

    render: function() {
        this.$el.html(this.template(this.group.toJSON()));
        this._attachEvents();
        return this;
    }
});