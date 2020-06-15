import React, { Fragment } from 'react';
import Form from './Form';
import Leads from './Leads';
import Search from './Search';

export default function Dashboard() {
  return (
    <Fragment>
      <br/>
      <br/>
      <Search />
      <br/>
      <Leads />
      <br/>
      <Form />
    </Fragment>
  );
}
