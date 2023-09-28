odoo.define('custom_pc_builder.pc_builder', function (require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');
    var ajax = require('web.ajax');
    var _t = core._t;
    var QWeb = core.qweb;

    var PCBuilder = Widget.extend({
        template: 'pc_builder_template',
        events: {
            'click .component-item': 'onComponentItemClick',
            'click .add-to-cart': 'onAddToCartClick',
        },

        start: function () {
            this.loadComponents();
            return this._super();
        },

        loadComponents: function () {
            var self = this;
            ajax.jsonRpc('/pc_builder/components', 'call', {}).then(function (data) {
                self.$('.components-list').html(QWeb.render('ComponentItems', {components: data}));
            });
        },

        onComponentItemClick: function (event) {
            var componentId = $(event.currentTarget).data('id');
            this.loadComponentDetails(componentId);
        },

        loadComponentDetails: function (componentId) {
            var self = this;
            ajax.jsonRpc('/pc_builder/component/' + componentId, 'call', {}).then(function (data) {
                self.$('.component-details').html(QWeb.render('ComponentDetails', {component: data}));
            });
        },

        onAddToCartClick: function () {
            var self = this;
            var selectedComponents = this.getSelectedComponents();
            ajax.jsonRpc('/pc_builder/add_to_cart', 'call', {components: selectedComponents}).then(function (data) {
                if (data.success) {
                    self.do_notify(_t('Success'), _t('The custom PC has been added to your cart.'));
                } else {
                    self.do_warn(_t('Error'), _t('There was an error adding the custom PC to your cart.'));
                }
            });
        },

        getSelectedComponents: function () {
            var selectedComponents = [];
            this.$('.component-item.selected').each(function () {
                selectedComponents.push($(this).data('id'));
            });
            return selectedComponents;
        },
    });

    return PCBuilder;
});