import { NgModule, NO_ERRORS_SCHEMA, ModuleWithProviders } from '@angular/core';
import { HomeComponent } from './home.component';
import { MDBBootstrapModulePro, ToastModule } from '../typescripts/pro/index';
import { MDBBootstrapModule } from 'app/typescripts/free';
import { HomeDataService } from 'app/home/home-data.service';
import { InfostripComponent } from './infostrip/infostrip.component';
import { CoursecontainerComponent } from './coursecontainer/coursecontainer.component';
import { CoursesComponent } from './courses/courses.component';
import { CommonModule } from '@angular/common';
import { BeinstructorComponent } from './beinstructor/beinstructor.component';
import { ForbusinessComponent } from './forbusiness/forbusiness.component';
import { PopularcoursesComponent } from './popularcourses/popularcourses.component';
import { LoaderComponent } from 'app/shared/loader/loader/loader.component';
import { StarRatingComponent } from '../shared/star-rating/star-rating.component';


@NgModule({
  imports: [
    MDBBootstrapModulePro.forRoot(),
    ToastModule.forRoot(),
    MDBBootstrapModule.forRoot(),
    MDBBootstrapModulePro.forRoot(),
    CommonModule
  ],
  declarations: [
    HomeComponent,
    InfostripComponent,
    CoursecontainerComponent,
    CoursesComponent,
    BeinstructorComponent,
    ForbusinessComponent,
    PopularcoursesComponent,
    LoaderComponent,
    StarRatingComponent
  ],
  exports: [HomeComponent, LoaderComponent, StarRatingComponent],
  providers: [HomeDataService],
  schemas: [NO_ERRORS_SCHEMA]
})
export class HomeModule {
  static forRoot(): ModuleWithProviders {
    return {
      ngModule: HomeModule,
      providers: [HomeDataService]
    };
  }
 }
