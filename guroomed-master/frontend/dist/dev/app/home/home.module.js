"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var home_component_1 = require("./home.component");
var home_routing_module_1 = require("./home-routing.module");
var shared_module_1 = require("../shared/shared.module");
var name_list_service_1 = require("../shared/name-list/name-list.service");
var head_component_1 = require("./head/head.component");
var infostrip_component_1 = require("./infostrip/infostrip.component");
var coursescontainer_component_1 = require("./coursescontainer/coursescontainer.component");
var course_component_1 = require("./course/course.component");
var beinstructor_component_1 = require("./beinstructor/beinstructor.component");
var forbusiness_component_1 = require("./forbusiness/forbusiness.component");
var footer_component_1 = require("./footer/footer.component");
var elasticsearch_module_1 = require("../elasticsearch/elasticsearch.module");
var HomeModule = (function () {
    function HomeModule() {
    }
    HomeModule = __decorate([
        core_1.NgModule({
            imports: [home_routing_module_1.HomeRoutingModule, shared_module_1.SharedModule, elasticsearch_module_1.ElasticsearchModule],
            declarations: [home_component_1.HomeComponent, head_component_1.HeadComponent, infostrip_component_1.InfostripComponent, coursescontainer_component_1.CoursescontainerComponent, course_component_1.CourseComponent, beinstructor_component_1.BeinstructorComponent,
                forbusiness_component_1.ForbusinessComponent, footer_component_1.FooterComponent],
            exports: [home_component_1.HomeComponent],
            providers: [name_list_service_1.NameListService]
        })
    ], HomeModule);
    return HomeModule;
}());
exports.HomeModule = HomeModule;

//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImFwcC9ob21lL2hvbWUubW9kdWxlLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7Ozs7Ozs7O0FBQUEsc0NBQXlDO0FBQ3pDLG1EQUFpRDtBQUNqRCw2REFBMEQ7QUFDMUQseURBQXVEO0FBQ3ZELDJFQUF3RTtBQUN4RSx3REFBb0Q7QUFDcEQsdUVBQW1FO0FBQ25FLDRGQUF3RjtBQUN4Riw4REFBMEQ7QUFDMUQsZ0ZBQTRFO0FBQzVFLDZFQUF5RTtBQUN6RSw4REFBMEQ7QUFDMUQsOEVBQTBFO0FBUzFFO0lBQUE7SUFBMEIsQ0FBQztJQUFkLFVBQVU7UUFQdEIsZUFBUSxDQUFDO1lBQ1IsT0FBTyxFQUFFLENBQUMsdUNBQWlCLEVBQUUsNEJBQVksRUFBRSwwQ0FBbUIsQ0FBQztZQUMvRCxZQUFZLEVBQUUsQ0FBQyw4QkFBYSxFQUFDLDhCQUFhLEVBQUUsd0NBQWtCLEVBQUMsc0RBQXlCLEVBQUUsa0NBQWUsRUFBRSw4Q0FBcUI7Z0JBQ2hJLDRDQUFvQixFQUFDLGtDQUFlLENBQUM7WUFDckMsT0FBTyxFQUFFLENBQUMsOEJBQWEsQ0FBQztZQUN4QixTQUFTLEVBQUUsQ0FBQyxtQ0FBZSxDQUFDO1NBQzdCLENBQUM7T0FDVyxVQUFVLENBQUk7SUFBRCxpQkFBQztDQUEzQixBQUEyQixJQUFBO0FBQWQsZ0NBQVUiLCJmaWxlIjoiYXBwL2hvbWUvaG9tZS5tb2R1bGUuanMiLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBOZ01vZHVsZSB9IGZyb20gJ0Bhbmd1bGFyL2NvcmUnO1xyXG5pbXBvcnQgeyBIb21lQ29tcG9uZW50IH0gZnJvbSAnLi9ob21lLmNvbXBvbmVudCc7XHJcbmltcG9ydCB7IEhvbWVSb3V0aW5nTW9kdWxlIH0gZnJvbSAnLi9ob21lLXJvdXRpbmcubW9kdWxlJztcclxuaW1wb3J0IHsgU2hhcmVkTW9kdWxlIH0gZnJvbSAnLi4vc2hhcmVkL3NoYXJlZC5tb2R1bGUnO1xyXG5pbXBvcnQgeyBOYW1lTGlzdFNlcnZpY2UgfSBmcm9tICcuLi9zaGFyZWQvbmFtZS1saXN0L25hbWUtbGlzdC5zZXJ2aWNlJztcclxuaW1wb3J0IHtIZWFkQ29tcG9uZW50fSBmcm9tICcuL2hlYWQvaGVhZC5jb21wb25lbnQnO1xyXG5pbXBvcnQge0luZm9zdHJpcENvbXBvbmVudH0gZnJvbSAnLi9pbmZvc3RyaXAvaW5mb3N0cmlwLmNvbXBvbmVudCc7XHJcbmltcG9ydCB7Q291cnNlc2NvbnRhaW5lckNvbXBvbmVudH0gZnJvbSAnLi9jb3Vyc2VzY29udGFpbmVyL2NvdXJzZXNjb250YWluZXIuY29tcG9uZW50JztcclxuaW1wb3J0IHtDb3Vyc2VDb21wb25lbnR9IGZyb20gJy4vY291cnNlL2NvdXJzZS5jb21wb25lbnQnO1xyXG5pbXBvcnQge0JlaW5zdHJ1Y3RvckNvbXBvbmVudH0gZnJvbSAnLi9iZWluc3RydWN0b3IvYmVpbnN0cnVjdG9yLmNvbXBvbmVudCc7XHJcbmltcG9ydCB7Rm9yYnVzaW5lc3NDb21wb25lbnR9IGZyb20gJy4vZm9yYnVzaW5lc3MvZm9yYnVzaW5lc3MuY29tcG9uZW50JztcclxuaW1wb3J0IHtGb290ZXJDb21wb25lbnR9IGZyb20gJy4vZm9vdGVyL2Zvb3Rlci5jb21wb25lbnQnO1xyXG5pbXBvcnQge0VsYXN0aWNzZWFyY2hNb2R1bGV9IGZyb20gJy4uL2VsYXN0aWNzZWFyY2gvZWxhc3RpY3NlYXJjaC5tb2R1bGUnO1xyXG5cclxuQE5nTW9kdWxlKHtcclxuICBpbXBvcnRzOiBbSG9tZVJvdXRpbmdNb2R1bGUsIFNoYXJlZE1vZHVsZSwgRWxhc3RpY3NlYXJjaE1vZHVsZV0sXHJcbiAgZGVjbGFyYXRpb25zOiBbSG9tZUNvbXBvbmVudCxIZWFkQ29tcG9uZW50LCBJbmZvc3RyaXBDb21wb25lbnQsQ291cnNlc2NvbnRhaW5lckNvbXBvbmVudCwgQ291cnNlQ29tcG9uZW50ICxCZWluc3RydWN0b3JDb21wb25lbnQsXHJcbiAgRm9yYnVzaW5lc3NDb21wb25lbnQsRm9vdGVyQ29tcG9uZW50XSxcclxuICBleHBvcnRzOiBbSG9tZUNvbXBvbmVudF0sXHJcbiAgcHJvdmlkZXJzOiBbTmFtZUxpc3RTZXJ2aWNlXVxyXG59KVxyXG5leHBvcnQgY2xhc3MgSG9tZU1vZHVsZSB7IH1cclxuIl19
