var AdminReductionView = BaseView.extend({
    template: _.template($('#generateReductionTemplate').html()),

    selectors: {
        groupPerMonth: '#group-per-month',
        facultyPerMonth: '#faculty-per-month',
        facultyPerSemester: '#faculty-per-semester',
        month: '#month',
        semester: '#semester',
        groupList: '#group-list',
        generateReductionButton: '.generate-reduction'
    },

    states: {
        groupPerMonth: function () {
            this._showGroupList();
            this._showMonth();
            this._hideSemester();
        },
        facultyPerMonth: function () {
            this._showMonth();
            this._hideGroupList();
            this._hideSemester();
        },
        facultyPerSemester: function () {
            this._showSemester();
            this._hideMonth();
            this._hideGroupList();
        }
    },

    initialize: function (options) {
        this.groupsCollection = options.groupsCollection;
        this.faculty = options.faculty
    },

    _delegateEvents: function () {
        this.$el.on('change', 'input[type=radio]', $.proxy(this._switchState, this));
        this.$(this.selectors.generateReductionButton).on('click', $.proxy(this._generateReduction, this))
    },

    _switchState: function (event) {
        this.states[event.target.value].call(this);
    },

    _showMonth: function () {
        this.$(this.selectors.month).parent().show();
    },

    _hideMonth: function () {
        this.$(this.selectors.month).parent().hide();
    },

    _renderGroupList: function () {
        this.groupsCollection.reduce(function (list, group) {
            var option = document.createElement('option');
            option.value = group.get('id');
            option.innerText = group.get('number');
            return list.add(option);
        }, $()).appendTo(
            this.$(this.selectors.groupList)
        );
    },

    _showGroupList: function () {
        if (!this.$(this.selectors.groupList).has('option').length) {
            this._renderGroupList();
        }
        this.$(this.selectors.groupList).parent().show();
    },

    _hideGroupList: function () {
        this.$(this.selectors.groupList).parent().hide();
    },

    _showSemester: function () {
        this.$(this.selectors.semester).parent().show();
    },

    _hideSemester: function () {
        this.$(this.selectors.semester).parent().hide();
    },

    _generateReduction: function () {
        var params = {
            type: this.$('input[name="type"]').val(),
            group: this.$(this.selectors.groupList).val(),
            month: this.$(this.selectors.month).val(),
            semester: this.$(this.selectors.semester).val(),
            faculty: this.faculty.get('id')
        };
        $.post('/app/reduction/', params).done(function (resp) {
            var a = document.createElement('a');
            var event = document.createEvent('Event');
            a.href = resp.url;
            a.download = _.last(resp.url.split('/'));
            a.target = '_blank';
            event.initEvent('click', true, true);
            a.dispatchEvent(event);
        });
    },

    render: function () {
        this.$el.html(this.template());
        this._delegateEvents();
        this.states.groupPerMonth.call(this);
        return this;
    }
});