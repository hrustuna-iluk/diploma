var ScheduleView = BaseView.extend({

    template:  _.template($("#scheduleTemplate").html()),

    initialize: function(options) {
        this.collection = options.collection;
        this.teacherCollection = options.teacherCollection;
        this.group = options.group;
    },

    _attachEvents: function() {
        this.$('.deleteSchedule').on('click', $.proxy(this._wantDeleteSchedule, this));
        this.$('select').on('change', $.proxy(this._buildScheduler, this));
    },

    _buildScheduler: function () {
        var numberOfClass = 1;
        this.$('table tbody').empty();
        while (numberOfClass !== 7) {
            this.$('table tbody').append(
                new ClassesView({
                    numberOfClass: numberOfClass,
                    numberOfWeek: this.$('select').val(),
                    group: this.group,
                    collection: this.collection,
                    teacherCollection: this.teacherCollection
                }).render().$el
            );
            numberOfClass++;
        }
    },

    _wantDeleteSchedule: function() {
        if(!confirm("Ви дійсно хочете видалити розклад?")) {
            return;
        }
        this._deleteSchedule();
    },

    _deleteSchedule: function() {

    },

    render: function() {
        this.$el.html(this.template);
        this._buildScheduler();
        this._attachEvents();
        return this;
    }
});