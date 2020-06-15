import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { searchLeads } from '../../actions/leads';

export class Search extends Component {
    state={
        search:''
    }
    static propTypes = {
        leads: PropTypes.array.isRequired,
        searchLeads: PropTypes.func.isRequired
    };

    onChange = (e) => this.setState({ [e.target.name]: e.target.value });

    onSubmit = (e) => {
        e.preventDefault();
        const { search } = this.state;
        this.props.searchLeads(search);
        this.setState({
          search:''
        });
    };

    render(){

        return(
            <Fragment>
                <form onSubmit={this.onSubmit}>
                    <div className="form-group">
                        <input
                        className="form-control"
                        type="text"
                        name="search"
                        placeholder="Search By Name And Place Enter"
                        onChange={this.onChange}
                        value={this.state.search}
                        />
                    </div>
                    <div className="form-group">
                </div>
                </form>
                {this.props.leads.length>0 && 
                <Fragment>
                <h2>Search Results</h2>
                <table className="table table-striped">
                <thead>
                    <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    {this.props.leads.map((lead) => (
                    <tr key={lead.id}>
                        <td>{lead.id}</td>
                        <td>{lead.name}</td>
                        <td>{lead.email}</td>
                    </tr>
                    ))}
                </tbody>
                </table>
                </Fragment>
                }
            </Fragment>
        );
    }
}

const mapStateToProps = (state) => ({
    leads: state.leads.searchResults,
  });

export default connect(mapStateToProps,{searchLeads})(Search);