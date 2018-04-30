__author__ = "Andre Barbe"
__project__ = "Auto-GTAP"
__created__ = "2018-3-13"
__altered__ = "2018-3-23"


class CreateSTI(object):
    """Creates an STI File for controlling SLTOHT
    SLTOHT exports variables from the .sl4 file to a .csv file
    The STI file tells SLTOHT where its input and output files are"""

    # Also creates STI files for PGSing .tab files

    __slots__ = ["input_file_name", "simulation_name", "sti_type"]

    def __init__(self, input_file_name: str, simulation_name: str, sti_type: str) -> None:
        self.input_file_name = input_file_name
        self.simulation_name = simulation_name
        self.sti_type = sti_type

        # Create list of lines to write to STI file
        if self.sti_type == "sltoht":
            line_list = [
                # First, select general options
                "bat         		! Run in batch. \n",
                "log		        ! Start a log file \n",
                "b		        	! Output to both terminal and log file \n",
                "sim_{0}_sltoth_sti.log	    	! Name of log file\n".format(self.simulation_name),
                "ses                ! Output to spreadsheet with element labels \n",
                ",                  ! Character to use for data separation \n",
                "shl                ! Show level results, if available \n",
                "                   ! Done selecting general options \n",
                "sim_{0}.sl4            ! Location of sl4 file to convert to csv \n".format(self.simulation_name),
                "c                  ! Want both levels and cumulative from solution file \n",
                "y                  ! Use file to choose which variables and components to ouptut \n",
                "sim_{0}.map            ! Name of file to use choosing which variables and components to output \n".format(
                    self.simulation_name),
                "sim_{0}.csv            ! Name of file to output to".format(self.simulation_name)
            ]
            output_file_name = "sim_{0}_sltoht".format(self.simulation_name)

        if self.sti_type == "gtap-e":
            line_list = [
                "!   gtap.sti \n",
                "! == == == == \n",
                "! \n",
                "!   TABLO sti file for GTAP 6.1 \n",
                "! \n",
                "bat         ! Run in batch. \n",
                " \n",
                "gtap        ! name of TABLO input file \n",
                "gtap        ! name of information file \n",
                "c           ! Perform condensation. \n",
                "o           ! Omit one or more variables. \n",
                "atall \n",
                "tf \n",
                " \n",
                "b           ! Substitute a variable and backsolve for it. \n",
                "pgd \n",
                "GHHDPRICE \n",
                "b \n",
                "pgm \n",
                "GHHIPRICES \n",
                "b \n",
                "pgt \n",
                "GCOMPRICE \n",
                "b \n",
                "qgm \n",
                "GHHLDAGRIMP \n",
                "b \n",
                "qgt \n",
                "QGTEQ \n",
                "b \n",
                "pgov \n",
                "GPRICEINDEX \n",
                "b \n",
                "qpt \n",
                "QPTEQ \n",
                "b \n",
                "ppd \n",
                "PHHDPRICE \n",
                "b \n",
                "ppm \n",
                "PHHIPRICES \n",
                "b \n",
                "qpm \n",
                "PHHLDAGRIMP \n",
                "b \n",
                "ppt \n",
                "PCOMPRICE \n",
                "b \n",
                "qft \n",
                "QFTEQ \n",
                "b \n",
                "pfd \n",
                "DMNDDPRICE \n",
                "b \n",
                "pfm \n",
                "DMNDIPRICES \n",
                "b \n",
                "pft \n",
                "ICOMPRICE \n",
                "b \n",
                "qfm \n",
                "INDIMP \n",
                "b \n",
                "ao \n",
                "AOWORLD \n",
                "b \n",
                "af \n",
                "AFWORLD \n",
                "b \n",
                "qfe \n",
                "QFEEQ \n",
                "b \n",
                "pfob \n",
                "EXPRICES \n",
                "b \n",
                "pms \n",
                "MKTPRICES \n",
                "b \n",
                "qtmfsd \n",
                "QTRANS_MFSD \n",
                "b \n",
                "ptrans \n",
                "TRANSCOSTINDEX \n",
                "b \n",
                "atmfsd \n",
                "TRANSTECHANGE \n",
                "b \n",
                "pcif \n",
                "FOBCIF \n",
                "b \n",
                "compvalad \n",
                "COMPVALADEQ \n",
                "b \n",
                "CNTqor \n",
                "CONT_EV_qor \n",
                "b \n",
                "CNTqoir \n",
                "CONT_EV_qoir \n",
                "b \n",
                "CNTqfer \n",
                "CONT_EV_qfer \n",
                "b \n",
                "CNTqfeir \n",
                "CONT_EV_qfeir \n",
                "b \n",
                "CNTqfeijr \n",
                "CONT_EV_qfeijr \n",
                "b \n",
                "CNTqfmr \n",
                "CONT_EV_qfmr \n",
                "b \n",
                "CNTqfmir \n",
                "CONT_EV_qfmir \n",
                "b \n",
                "CNTqfmijr \n",
                "CONT_EV_qfmijr \n",
                "b \n",
                "CNTqfdr \n",
                "CONT_EV_qfdr \n",
                "b \n",
                "CNTqfdir \n",
                "CONT_EV_qfdir \n",
                "b \n",
                "CNTqfdijr \n",
                "CONT_EV_qfdijr \n",
                "b \n",
                "CNTqpmr \n",
                "CONT_EV_qpmr \n",
                "b \n",
                "CNTqpmir \n",
                "CONT_EV_qpmir \n",
                "b \n",
                "CNTqpdr \n",
                "CONT_EV_qpdr \n",
                "b \n",
                "CNTqpdir \n",
                "CONT_EV_qpdir \n",
                "b \n",
                "CNTqgmr \n",
                "CONT_EV_qgmr \n",
                "b \n",
                "CNTqgmir \n",
                "CONT_EV_qgmir \n",
                "b \n",
                "CNTqgdr \n",
                "CONT_EV_qgdr \n",
                "b \n",
                "CNTqgdir \n",
                "CONT_EV_qgdir \n",
                "b \n",
                "CNTqxsr \n",
                "CONT_EV_qxsr \n",
                "b \n",
                "CNTqxsirs \n",
                "CONT_EV_qxsirs \n",
                "b \n",
                "CNTqimr \n",
                "CONT_EV_qimr \n",
                "b \n",
                "CNTqimisr \n",
                "CONT_EV_qimisr \n",
                "b \n",
                "CNTalleffr \n",
                "CONT_EV_alleffr \n",
                "b \n",
                "CNTtotr \n",
                "CONT_EV_totr \n",
                "b \n",
                "CNTtech_aoir \n",
                "CONT_EV_tech_aoir \n",
                "b \n",
                "CNTtech_afijr \n",
                "CONT_EV_tech_afijr \n",
                "b \n",
                "CNTtech_afmfdsd \n",
                "CONT_EV_tech_afmfdsd \n",
                "b \n",
                "CNTtech_amsirs \n",
                "CONT_EV_tech_amsirs \n",
                "e           ! Exit condensation. \n",
                "a           ! Proceed to automatic code generation. \n",
                "pgs         ! Write a GEMSIM program. \n",
                " \n",
                "gtap        ! name of program file \n",
                "! \n",
                "! \n",
                "!   end of stored input \n",
                "!   ------------------- \n"
            ]
            output_file_name = self.input_file_name

        if self.sti_type == "gtap-v7":
            line_list = [
                "!___________________________start of GTAP.STI file_____________________\n",
                "!\n",
                "bat       ! This runs in batch mode\n",
                "\n",
                "gtap      ! file output .tab\n",
                "gtap      ! file output .inf\n",
                "c         ! choose condensation\n",
                "o         ! begin with ommitting the unnecessary policy variables\n",
                "tf\n",
                "tpm\n",
                "tpd\n",
                "tgm\n",
                "tgd\n",
                "tfm\n",
                "tfd\n",
                "atall     ! omit the four-dimensional shock to margins tech change\n",
                "! aoall   leave in for gtaptech version for chp11 and chp13\n",
                "avaall    ! omit the three-dimensional shock to value added tech change\n",
                "! afall   leave in for gtaptech version for chp11 and chp13\n",
                "! afeall  leave in for gtaptech version for chp11 and chp13\n",
                "\n",
                "b\n",
                "pfd\n",
                "DMNDDPRICE\n",
                "b\n",
                "compvalad\n",
                "compvaladeq\n",
                "b\n",
                "af\n",
                "AFWORLD   ! added JMH june 7 2000 to evade need for GEMPACK licence on CHP10\n",
                "b\n",
                "ao\n",
                "AOWORLD   ! added JMH june 7 2000 to evade need for GEMPACK licence on CHP10\n",
                "b\n",
                "ava\n",
                "AVAWORLD   ! added JMH june 7 2000 to evade need for GEMPACK licence on CHP10\n",
                "b\n",
                "afe\n",
                "AFEWORLD   ! added JMH june 7 2000 to evade need for GEMPACK licence on CHP10\n",
                "b\n",
                "ppm\n",
                "PHHIPRICES\n",
                "b\n",
                "pfm\n",
                "DMNDIPRICES\n",
                "b\n",
                "pms\n",
                "MKTPRICES\n",
                "b\n",
                "pfob\n",
                "EXPRICES\n",
                "b\n",
                "pcif\n",
                "FOBCIF\n",
                "b\n",
                "pf\n",
                "ICOMPRICE\n",
                "b\n",
                "ppd\n",
                "PHHDPRICE\n",
                "b\n",
                "pgm\n",
                "GHHIPRICES\n",
                "b\n",
                "pgd\n",
                "GHHDPRICE\n",
                "b\n",
                "qfm\n",
                "INDIMP\n",
                "!b     needed for geelas\n",
                "!qfd\n",
                "!INDDOM\n",
                "b\n",
                "pvaen\n",
                "VAPRICE\n",
                "!b          this has been suppressed by JMB Sept. 2001\n",
                "!qfe\n",
                "!ENDWDEMAND\n",
                "b\n",
                "qvaen\n",
                "VADEMAND\n",
                "b\n",
                "qf\n",
                "INTDEMAND\n",
                "b\n",
                "pgov\n",
                "GPRICEINDEX\n",
                "b\n",
                "qg\n",
                "GOVDMNDS\n",
                "b\n",
                "pg\n",
                "GCOMPRICE\n",
                "b\n",
                "qgm\n",
                "GHHLDAGRIMP\n",
                "!b    needed for GEELAS\n",
                "!qgd\n",
                "!GHHLDDOM\n",
                "b\n",
                "qp\n",
                "PRIVDMNDS\n",
                "!b   needed for geelas\n",
                "!qpd\n",
                "!PHHLDDOM\n",
                "b\n",
                "qpm\n",
                "PHHLDAGRIMP\n",
                "b           ! These are new backsolves associated with trade and transport\n",
                "qtmfsd\n",
                "QTRANS_MFSD\n",
                "b\n",
                "ptrans\n",
                "TRANSCOSTINDEX\n",
                "b\n",
                "atmfsd\n",
                "TRANSTECHANGE\n",
                "b           ! Backsolves and substitutions associated with welfare decomposition\n",
                "CNTqor\n",
                "CONT_EV_qor\n",
                "b\n",
                "CNTqoir\n",
                "CONT_EV_qoir\n",
                "b\n",
                "CNTqfer\n",
                "CONT_EV_qfer\n",
                "b\n",
                "CNTqfeir\n",
                "CONT_EV_qfeir\n",
                "! Summary variables not used in DECOMP have been commented out of GTAP.TAB\n",
                "!s\n",
                "!CNTqfejr\n",
                "!CONT_EV_qfejr\n",
                "b\n",
                "CNTqfeijr\n",
                "CONT_EV_qfeijr\n",
                "b\n",
                "CNTqfmr\n",
                "CONT_EV_qfmr\n",
                "b\n",
                "CNTqfmir\n",
                "CONT_EV_qfmir\n",
                "!s\n",
                "!CNTqfmjr\n",
                "!CONT_EV_qfmjr\n",
                "b\n",
                "CNTqfmijr\n",
                "CONT_EV_qfmijr\n",
                "b\n",
                "CNTqfdr\n",
                "CONT_EV_qfdr\n",
                "b\n",
                "CNTqfdir\n",
                "CONT_EV_qfdir\n",
                "!s\n",
                "!CNTqfdjr\n",
                "!CONT_EV_qfdjr\n",
                "b\n",
                "CNTqfdijr\n",
                "CONT_EV_qfdijr\n",
                "b\n",
                "CNTqpmr\n",
                "CONT_EV_qpmr\n",
                "b\n",
                "CNTqpmir\n",
                "CONT_EV_qpmir\n",
                "b\n",
                "CNTqpdr\n",
                "CONT_EV_qpdr\n",
                "b\n",
                "CNTqpdir\n",
                "CONT_EV_qpdir\n",
                "b\n",
                "CNTqgmr\n",
                "CONT_EV_qgmr\n",
                "b\n",
                "CNTqgmir\n",
                "CONT_EV_qgmir\n",
                "b\n",
                "CNTqgdr\n",
                "CONT_EV_qgdr\n",
                "b\n",
                "CNTqgdir\n",
                "CONT_EV_qgdir\n",
                "b\n",
                "CNTqxsr\n",
                "CONT_EV_qxsr\n",
                "!s\n",
                "!CNTqxsir\n",
                "!CONT_EV_qxsir\n",
                "!s\n",
                "!CNTqxsrs\n",
                "!CONT_EV_qxsrs\n",
                "b\n",
                "CNTqxsirs\n",
                "CONT_EV_qxsirs\n",
                "b\n",
                "CNTqimr\n",
                "CONT_EV_qimr\n",
                "!s\n",
                "!CNTqimir\n",
                "!CONT_EV_qimir\n",
                "!s\n",
                "!CNTqimsr\n",
                "!CONT_EV_qimsr\n",
                "b\n",
                "CNTqimisr\n",
                "CONT_EV_qimisr\n",
                "b\n",
                "CNTalleffr\n",
                "CONT_EV_alleffr\n",
                "!s\n",
                "!CNTtech_atrisr\n",
                "!CONT_EV_tech_atrisr\n",
                "b\n",
                "CNTtotr\n",
                "CONT_EV_totr\n",
                "b\n",
                "CNTtech_avajr\n",
                "CONT_EV_tech_avajr\n",
                "!s\n",
                "!CNTtech_afjr\n",
                "!CONT_EV_tech_afjr\n",
                "b\n",
                "CNTtech_aoir\n",
                "CONT_EV_tech_aoir\n",
                "!s\n",
                "!CNTtech_afejr\n",
                "!CONT_EV_tech_afejr\n",
                "b\n",
                "CNTtech_afeijr\n",
                "CONT_EV_tech_afeijr\n",
                "!s\n",
                "!CNTtech_atrir\n",
                "!CONT_EV_tech_atrir\n",
                "!s\n",
                "!CNTtech_atrsr\n",
                "!CONT_EV_tech_atrsr\n",
                "b\n",
                "CNTtech_afmfdsd\n",
                "CONT_EV_tech_afmfdsd\n",
                "b\n",
                "CNTtech_afijr\n",
                "CONT_EV_tech_afijr\n",
                "!s\n",
                "!CNTtech_afir\n",
                "!CONT_EV_tech_afir\n",
                "b\n",
                "CNTtech_amsirs\n",
                "CONT_EV_tech_amsirs\n",
                "! End of backsolves and substitutions associated with welfare decomposition\n",
                "e           ! exit condensation\n",
                "a           ! automatic code generation\n",
                "! pgs       ! prepare for GEMSIM\n",
                "wfp      	! write TABLO-generated program\n",
                "\n",
                "GTAP       ! Name of program\n",
                "!________________________________end of file_____________________"
            ]
            output_file_name = self.input_file_name


        # Create final file
        with open("{0}.sti".format(output_file_name), "w+") as writer:  # Create the empty file
            writer.writelines(line_list)  # write the line list to the file
