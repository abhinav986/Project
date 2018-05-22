"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var common_1 = require("@angular/common");
var about_component_1 = require("./about.component");
var about_routing_module_1 = require("./about-routing.module");
var AboutModule = (function () {
    function AboutModule() {
    }
    AboutModule = __decorate([
        core_1.NgModule({
            imports: [common_1.CommonModule, about_routing_module_1.AboutRoutingModule],
            declarations: [about_component_1.AboutComponent],
            exports: [about_component_1.AboutComponent]
        })
    ], AboutModule);
    return AboutModule;
}());
exports.AboutModule = AboutModule;

//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImFwcC9hYm91dC9hYm91dC5tb2R1bGUudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7QUFBQSxzQ0FBeUM7QUFDekMsMENBQStDO0FBQy9DLHFEQUFtRDtBQUNuRCwrREFBNEQ7QUFPNUQ7SUFBQTtJQUEyQixDQUFDO0lBQWYsV0FBVztRQUx2QixlQUFRLENBQUM7WUFDUixPQUFPLEVBQUUsQ0FBQyxxQkFBWSxFQUFFLHlDQUFrQixDQUFDO1lBQzNDLFlBQVksRUFBRSxDQUFDLGdDQUFjLENBQUM7WUFDOUIsT0FBTyxFQUFFLENBQUMsZ0NBQWMsQ0FBQztTQUMxQixDQUFDO09BQ1csV0FBVyxDQUFJO0lBQUQsa0JBQUM7Q0FBNUIsQUFBNEIsSUFBQTtBQUFmLGtDQUFXIiwiZmlsZSI6ImFwcC9hYm91dC9hYm91dC5tb2R1bGUuanMiLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBOZ01vZHVsZSB9IGZyb20gJ0Bhbmd1bGFyL2NvcmUnO1xyXG5pbXBvcnQgeyBDb21tb25Nb2R1bGUgfSBmcm9tICdAYW5ndWxhci9jb21tb24nO1xyXG5pbXBvcnQgeyBBYm91dENvbXBvbmVudCB9IGZyb20gJy4vYWJvdXQuY29tcG9uZW50JztcclxuaW1wb3J0IHsgQWJvdXRSb3V0aW5nTW9kdWxlIH0gZnJvbSAnLi9hYm91dC1yb3V0aW5nLm1vZHVsZSc7XHJcblxyXG5ATmdNb2R1bGUoe1xyXG4gIGltcG9ydHM6IFtDb21tb25Nb2R1bGUsIEFib3V0Um91dGluZ01vZHVsZV0sXHJcbiAgZGVjbGFyYXRpb25zOiBbQWJvdXRDb21wb25lbnRdLFxyXG4gIGV4cG9ydHM6IFtBYm91dENvbXBvbmVudF1cclxufSlcclxuZXhwb3J0IGNsYXNzIEFib3V0TW9kdWxlIHsgfVxyXG4iXX0=
