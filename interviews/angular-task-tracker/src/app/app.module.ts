import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

import { AppRoutingModule } from 'src/app/app-routing.module'; // CLI imports AppRoutingModule

import { AppComponent } from 'src/app/app.component';
import { TasksComponent } from 'src/app/components/tasks/tasks.component';
import { AboutComponent } from 'src/app/components/about/about.component';
import { HeaderComponent } from 'src/app/components/header/header.component';
import { FooterComponent } from 'src/app/components/footer/footer.component';
import { ButtonComponent } from 'src/app/components/button/button.component';
import { AddTaskComponent } from 'src/app/components/add-task/add-task.component';
import { TaskItemComponent } from 'src/app/components/task-item/task-item.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    TasksComponent,
    TaskItemComponent,
    ButtonComponent,
    AboutComponent,
    AddTaskComponent,
  ],
  imports: [
    BrowserModule,
    FontAwesomeModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule, // CLI adds AppRoutingModule to the AppModule's imports array
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
