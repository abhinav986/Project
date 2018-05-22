import { NgModule } from '@angular/core';
import { HomeComponent } from './home.component';
import { HomeRoutingModule } from './home-routing.module';
import { SharedModule } from '../shared/shared.module';
import { NameListService } from '../shared/name-list/name-list.service';
import {HeadComponent} from './head/head.component';
import {InfostripComponent} from './infostrip/infostrip.component';
import {CoursescontainerComponent} from './coursescontainer/coursescontainer.component';
import {CourseComponent} from './course/course.component';
import {BeinstructorComponent} from './beinstructor/beinstructor.component';
import {ForbusinessComponent} from './forbusiness/forbusiness.component';
import {FooterComponent} from './footer/footer.component';
import {ElasticsearchModule} from '../elasticsearch/elasticsearch.module';

@NgModule({
  imports: [HomeRoutingModule, SharedModule, ElasticsearchModule],
  declarations: [HomeComponent,HeadComponent, InfostripComponent,CoursescontainerComponent, CourseComponent ,BeinstructorComponent,
  ForbusinessComponent,FooterComponent],
  exports: [HomeComponent],
  providers: [NameListService]
})
export class HomeModule { }
