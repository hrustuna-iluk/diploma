var IndividualWorkTabFormView = BaseView.extend({

     template: _.template($("#individualWorkTabFormTemplate").html()),

    selectors: {
        individualWorkTitleInput: '#individualWorkTitle',
        individualWorkYearInput: '#individualWorkYear',
        createIndividualWork: '#addIndividualWork',
        changeIndividualWork: '#changeIndividualWork'
    },

    initialize: function(options) {
        this.collection = options.workWithStudentCollection;
        this.publisher.on('change:individual:work', $.proxy(this._onIndividualWorkChange, this));
    },

    _attachEvents: function() {
        this.$(this.selectors.createIndividualWork).on('click', $.proxy(this._createIndividualWork, this));
        this.$(this.selectors.changeIndividualWork).on('click', $.proxy(this._changeIndividualWork, this));
    },

    _onIndividualWorkChange: function(model) {
        $(this.selectors.individualWorkTitleInput).val(model.getTitle());
        $(this.selectors.individualWorkYearInput).val(model.getYear());
        this.$(this.selectors.changeIndividualWork).data('model', model);
        this.$(this.selectors.createIndividualWork).addClass('no-display');
        this.$(this.selectors.changeIndividualWork).removeClass('no-display');
    },

    _individualWorkData: function(model) {
        model.setTitle(this.$(this.selectors.individualWorkTitleInput).val());
        model.setYear(this.$(this.selectors.individualWorkYearInput).val());
        this.$(this.selectors.individualWorkTitleInput).val("");
        this.$(this.selectors.individualWorkYearInput).val("");
    },

    _createIndividualWork: function() {
        var individualWorkModel = new WorkWithStudentModel({
            group: this.group.get('id')
        });
        this._individualWorkData(individualWorkModel);
        individualWorkModel.save({wait: true}, {success: $.proxy(function() {
                    this.collection.add(individualWorkModel);
                }, this)})
    },

    _changeIndividualWork: function() {
        var individualWorkModel = this.$(this.selectors.changeIndividualWork).data('model');
        this._individualWorkData(individualWorkModel);
        individualWorkModel.save();
        this.$(this.selectors.changeIndividualWork).addClass('no-display');
        this.$(this.selectors.createIndividualWork).removeClass('no-display');
    },

    render: function() {
        this.$el.html(this.template);
        this._attachEvents();
        return this;
    }

});