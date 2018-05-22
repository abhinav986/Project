import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthGuardService } from 'app/admin/services/auth-guard.service';
import { Routes, RouterModule } from '@angular/router';
import { MycoursesComponent } from 'app/mycourses/mycourses.component';
import { LearningComponent } from 'app/mycourses/learning/learning.component';
import { LecturesComponent } from 'app/mycourses/lectures/lectures.component';
import { ToastModule, MDBBootstrapModulePro } from 'app/typescripts/pro';
import { MDBBootstrapModule } from 'app/typescripts/free';
import { SafePipe } from './safe.pipe';
import { MycoursesService } from './mycourses.service';
import { HomeComponent } from '../home/home.component';
import { SideNavComponent } from './side-nav/side-nav.component';
import { NgxPaginationModule } from 'ngx-pagination';

const myCourseRoutes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'mycourses',
    canActivate: [AuthGuardService],
    component: LearningComponent
  },
  {
    path: 'instructor/course/draft-content/lecture',
    canActivate: [AuthGuardService],
    component: LecturesComponent
  },
  {
    path: 'instructor/course/draft-content/quiz',
    canActivate: [AuthGuardService],
    component: LecturesComponent
  },
  {
    path: 'lectures',
    canActivate: [AuthGuardService],
    component: LecturesComponent
  }
];

@NgModule({
  imports: [
    CommonModule,
    NgxPaginationModule,
    RouterModule.forChild(myCourseRoutes),
    ToastModule.forRoot(),
    MDBBootstrapModule.forRoot(),
    MDBBootstrapModulePro.forRoot(),
  ],
  exports: [
    RouterModule
  ],
  declarations: [
    MycoursesComponent,
    LearningComponent,
    LecturesComponent,
    SafePipe,
    SideNavComponent,
  ],
  providers: [
    AuthGuardService,
    MycoursesService
  ]
})
export class MycoursesModule { }
