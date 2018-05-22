import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EssearchComponent } from './essearch/essearch.component';

@NgModule({
  imports: [
    CommonModule
  ],
  exports:[EssearchComponent],
  declarations: [EssearchComponent]
})
export class ElasticsearchModule { }
